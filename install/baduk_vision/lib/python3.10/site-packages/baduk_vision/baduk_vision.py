import rclpy as rp
from rclpy.node import Node
from baduk_msgs.msg import Vision, State
from baduk_msgs.srv import Initialize
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import json
import os.path
import os
import matplotlib.pyplot as plt

import torch
from torchvision import transforms
from PIL import Image as PILImage
import baduk_vision.VisionModule.lenetgo as lenetgo

from baduk_vision.VisionModule import *

import threading

class BadukVision(Node):

    def __init__(self):
        super().__init__('baduk_vision')
        self.img_lock = threading.Lock()

        # Image subscriber
        self.imgSubscriber = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            10
        )
        self.bridge = CvBridge()
        self.img = None
        self.gray = None
        self.prev_gray = None
        self.pprev_gray = None
        self.check_color = False
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        #self.model = lenetgo.LeNetGo3()
        #self.model.load_state_dict(torch.load('./model/lenetgo_model_epoch74.pth'))
        self.model = lenetgo.LeNetGo2()
        self.model.load_state_dict(torch.load('/home/capstone/Go_bot/model/lenetgo_model_epoch30.pth')) #13 canny, 11 otsu
        self.model.to(self.device)
        self.transform = transforms.Compose([
                            transforms.Resize((32,32)),
                            transforms.Grayscale(num_output_channels=1),
                            transforms.ToTensor(),
                            transforms.Normalize(mean=[0.5], std=[0.5,])
                        ])

        # Service for do_initialize client
        self.initializeService = self.create_service(
            Initialize,
            'do_initialize',
            self.initialize_points
        )
        self.points = None

        # Service for check_vision client
        self.checkVisionSubscriber = self.create_subscription(
            Vision,
            'check_vision',
            self.check_board,
            10
        )
        self.prev_check = False

        # Publisher for game_state
        self.statePublisher = self.create_publisher(
            State,
            'game_state',
            10
        )
        self.timer = self.create_timer(0.5, self.state_callback)
        self.game_state = "."*361

        self.cornerPoints = np.float32([[326, 104], [1020, 112], [1210, 914], [150, 900]])
        self.start_flag = True

    def otsu_binarization(self, img):
        np_img = np.array(img)
        #np_img = cv2.Canny(np_img, 25, 100)
        _, otsu = cv2.threshold(np_img, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return PILImage.fromarray((otsu * 255).astype(np.uint8))

    def image_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            self.gray = cv2.cvtColor(perspective(self.cornerPoints, self.img), cv2.COLOR_BGR2GRAY)
            
            if self.start_flag:
                self.prev_gray = self.gray
                self.pprev_gray = self.gray
                self.start_flag = False
            
            flow = cv2.calcOpticalFlowFarneback(self.prev_gray, self.gray, 0.0, 0.5, 3, 15, 3, 5, 1.1, 0)
            
            if np.max(flow) > 3: #1.5:
                self.check_color = False
                self.get_logger().info(f'Motion Detected!')
            else:
                self.check_color = True
            
            if self.img is not None:
                self.get_logger().info("Image successfully converted to OpenCV format")
            else:
                self.get_logger().error("Failed to convert image")
                return
            
            if self.points is None:
                if not os.path.isfile('/home/capstone/Go_bot/points.json'):
                    self.get_logger().error(f'Initialize First!')
                else:
                    with open('/home/capstone/Go_bot/points.json', 'r') as jsonfile:
                        self.points = json.load(jsonfile)
            else:
                if (self.img.size != 0) and (self.points is not None) and self.check_color:
                    
                    img_transformed = perspective(self.cornerPoints, self.img)
                    
                    cv2.imwrite("/home/capstone/Go_bot/testImg.jpg", img_transformed)
                    
                    self.game_state = ""
                    for col in self.points:
                        for (x, y) in col:

                            x1 = max(0, x - 15)
                            y1 = max(0, y - 15)
                            x2 = min(self.img.shape[1], x + 16) 
                            y2 = min(self.img.shape[0], y + 16)

                            cropped = self.gray[int(y1):int(y2), int(x1):int(x2)]
                            
                            image = PILImage.fromarray(cropped)
                            image = self.transform(image).unsqueeze(0)

                            image = image.to(self.device)

                            with torch.no_grad():
                                outputs = self.model(image)

                            """
                            output = torch.argmax(outputs)
                            if output == 0:
                                self.game_state += 'b'
                            elif output == 1:
                                self.game_state += '.'
                            else:
                                self.game_state += 'w'
                            """
                            output = outputs[0][0].item()
                            if output < 0.5:
                                if np.mean(cropped) > 150:
                                    self.game_state += "w"
                                else:
                                    self.game_state += "b"
                            else:
                                self.game_state += '.'
                self.get_logger().info("state: "+ self.game_state)

            self.pprev_gray = self.prev_gray
            self.prev_gray = self.gray
                    
            
        except Exception as e:
            print(e)
            
    def initialize_points(self, req, res):
        if req.do_initialize:
            #img = homomorphic_filter(self.img)
            img = perspective(self.cornerPoints, self.img)
            blur = cv2.GaussianBlur(img, (0, 0), 1)
            gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
            #clahe = CLAHE(gray)
            canny = cv2.Canny(gray, 35, 40)
            

            lines = line_detector(canny)
            self.points = get_points(lines, 30)
           
            print(self.points)

            test_img = img.copy()
            for col in self.points:
                for (x, y) in col:
                    cv2.circle(test_img, (int(x), int(y)), 12, (255, 0, 0), -1)
            cv2.imwrite("/home/capstone/Go_bot/points.png", test_img)

            file = '/home/capstone/Go_bot/points.json'
            with open(file, 'w') as json_file:
                json.dump(self.points, json_file)

            res.done_initialize = True

            print("Successfully Get Points!")
            return res
        else:
            res.done_initialize = False

            return res

    def check_board(self, msg):
        print(msg.check_vision, self.prev_check)
        if msg.check_vision and (not self.prev_check):
            pass
    
    def state_callback(self):
        msg = State()

        msg.state = self.game_state[:: -1]

        self.statePublisher.publish(msg)
        #self.get_logger().info(f'{msg.state}')


def main(args=None):
    rp.init(args=args)

    badukVision = BadukVision()
    rp.spin(badukVision)

    cv2.destroyAllWindows()
    badukVision.destroy_node()
    rp.shutdown

if __name__ == '__main__':
    main()
