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

from baduk_vision.VisionModule import *

import threading

class BadukVision(Node):

    def __init__(self):
        super().__init__('baduk_vision')
        self.img_lock = threading.Lock()

        # Image subscriber
        self.imgSubscriber = self.create_subscription(
            Image,
            '/image_raw',
            self.image_callback,
            10
        )
        self.bridge = CvBridge()
        self.img = None

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

        # topLeft, topRight, bottomRight, bottomLeft
        # 2560,1440
        #self.cornerPoints = np.float32([[565, 49], [1755, 37], [2126, 1348], [294, 1425]])
        # 1280, 720
        self.cornerPoints = np.float32([[281, 24], [878, 19], [1065, 668], [143, 707]])

    def image_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            
            if self.img is not None:
                self.get_logger().info("Image successfully converted to OpenCV format")
            else:
                self.get_logger().error("Failed to convert image")
                return
                
            if self.points == None:
                if not os.path.isfile('./points.json'):
                    self.get_logger().error(f'Initialize First!')
                else:
                    with open('./points.json', 'r') as jsonfile:
                        self.points = json.load(jsonfile)
            else:
                if (self.img.size != 0) and (self.points is not None):
                    #cv2.imwrite("./check.png", self.img)
                    img_filtered = homomorphic_filter(self.img)
                    
                    img_transformed = perspective(self.cornerPoints, img_filtered)
                    img_transformed = CLAHE(img_transformed)
                    
                    #cv2.imwrite("./writtenImg.jpg", img_transformed)
                    
                    _, S, V = cv2.split(cv2.cvtColor(cv2.GaussianBlur(img_transformed, (0, 0), 3), cv2.COLOR_BGR2HSV))
                    data = np.empty((0, 2))
                    
                    self.game_state = ""
                    for col in self.points:
                        for (x, y) in col:
                            pts = [int(x), int(y)]

                            s = np.sum(S[pts[1] - 5:pts[1] + 6, pts[0] - 5:pts[0] + 6]) / (10 ** 2)
                            v = np.sum(V[pts[1] - 5:pts[1] + 6, pts[0] - 5:pts[0] + 6]) / (10 ** 2)
                            data = np.append(data, [[s, v]], axis=0)
                            if v <= 70:
                                self.game_state += "b"
                            elif v >= 180:
                                self.game_state += "w"
                            else:
                                self.game_state += "."
                print(self.game_state)
                    
            
        except Exception as e:
            print(e)
            
    def initialize_points(self, req, res):
        if req.do_initialize:
            img = homomorphic_filter(self.img)
            img = perspective(self.cornerPoints, img)
            blur = cv2.GaussianBlur(img, (0, 0), 1)
            gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
            clahe = CLAHE(gray)
            canny = cv2.Canny(clahe, 35, 40)
            

            lines = line_detector(canny)
            self.points = get_points(lines, 30)

            print(self.points)

            test_img = img.copy()
            for col in self.points:
                for (x, y) in col:
                    cv2.circle(test_img, (int(x), int(y)), 5, (255, 0, 0), -1)
            cv2.imwrite("./points.png", test_img)
            #cv2.imshow("vision", img)
            #cv2.waitKey(1)

            file = './points.json'
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

        msg.state = self.game_state

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
