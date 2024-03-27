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

class BadukVision(Node):

    def __init__(self):
        super().__init__('baduk_vision')

        # Image subscriber
        self.imgSubscriber = self.create_subscription(
            Image,
            'image_raw',
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
        self.subscriptions

        # Publisher for game_state
        self.statePublisher = self.create_publisher(
            State,
            'game_state',
            10
        )
        self.timer = self.create_timer(0.5, self.state_callback)
        self.game_state = "." * 361

        # topLeft, topRight, bottomRight, bottomLeft
        self.cornerPoints = np.float32([[147, 29], [486, 45], [600, 440], [30, 433]])

    def image_callback(self, msg):
        try:
            # line detect for initialize 나중에 밑 내용은 initialize 관련 함수로 옮길 예정
            self.img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
            
            if self.points == None:
                if not os.path.isfile('./points.json'):
                    self.get_logger().error(f'Initialize First!')
                else:
                    with open('./points.json', 'r') as jsonfile:
                        self.points = json.load(jsonfile)

            H, S, V = cv2.split(cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV))
            data = np.empty((0, 2))
            
            for col in self.points:
                for (x, y) in col:
                    pts = [int(x), int(y)]

                    s = np.sum(S[pts[1] - 10:pts[1] + 10, pts[0] - 10:pts[0] + 10]) / 20 ** 2
                    v = np.sum(V[pts[1] - 10:pts[1] + 10, pts[0] - 10:pts[0] + 10]) / 20 ** 2
                    data = np.append([s, v], axis=0)

            plt.scatter(data[:, 0], data[:, 1])
            plt.show()
            
        except Exception as e:
            print(e)
            
    def initialize_points(self, req, res):
        if req.do_initialize:
            img = perspective(self.cornerPoints, self.img)
            blur = cv2.GaussianBlur(img, (0, 0), 1)
            gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
            clahe = CLAHE(gray)
            canny = cv2.Canny(clahe, 35, 40)

            lines = line_detector(canny)
            self.points = get_points(lines, 10)

            """for (x, y) in self.points:
                cv2.circle(img, (int(x), int(y)), 1, (255, 0, 0), -1)

            cv2.imshow("vision", img)
            cv2.waitKey(1)"""

            file = './points.json'
            with open(file, 'w') as json_file:
                json.dump(self.points, json_file)

            res.done_initialize = True

            return res
        else:
            res.done_initialize = False

            return res

    def check_board(self, msg):
        if(msg.do_check and (not self.prev_check)):
            # Todo: get coord from file and calc color, save game_state
            pass
        self.prev_check = msg.do_check
    
    def state_callback(self):
        msg = State()

        msg.state = self.game_state


def main(args=None):
    rp.init(args=args)

    badukVision = BadukVision()
    rp.spin(badukVision)

    cv2.destroyAllWindows()
    badukVision.destroy_node()
    rp.shutdown

if __name__ == '__main__':
    main()
