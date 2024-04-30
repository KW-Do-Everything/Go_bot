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

        # optical flow를 위해 perspective 변환한 이미지를 gray로 변환, 이전 프레임의 gray도 저장
        self.gray = None
        self.prev_gray = None

        self.check_color = False

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = lenetgo.LeNetGo2()
        self.model.load_state_dict(torch.load('/home/capstone2/Go_bot/model/lenetgo_model_epoch30.pth'))
        self.model.to(self.device)
        self.transform = transforms.Compose([
                            transforms.Resize((32,32)),                     # 32x32로 resize
                            transforms.Grayscale(num_output_channels=1),    # grayscale 변환
                            transforms.ToTensor(),                          # 텐서로 변환
                            transforms.Normalize(mean=[0.5], std=[0.5,])    # 평균 0.5, 표준편차 0.5로 정규화
                        ])

        # Service for do_initialize client
        self.initializeService = self.create_service(
            Initialize,
            'do_initialize',
            self.initialize_points
        )
        self.points = None

        # Publisher for game_state
        self.statePublisher = self.create_publisher(
            State,
            'game_state',
            10
        )
        self.timer = self.create_timer(0.5, self.state_callback)
        self.game_state = "."*361

        self.cornerPoints = np.float32([[326, 104], [1015, 112], [1205, 905], [155, 900]])
        self.start_flag = True


    # 이미지가 들어오는 이미지 구독 노드
    def image_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')   # cv2 이미지로 변환
            self.gray = cv2.cvtColor(perspective(self.cornerPoints, self.img), cv2.COLOR_BGR2GRAY)
            
            # 이전 프레임 초기화
            # 처음 켰을 때 이전 프레임 gray를 현재 gray로 초기화 하고 start_flag를 False로
            if self.start_flag:
                self.prev_gray = self.gray
                self.start_flag = False
            
            # Optical Flow 계산
            flow = cv2.calcOpticalFlowFarneback(self.prev_gray, self.gray, 0.0, 0.5, 3, 15, 3, 5, 1.1, 0)
            
            # 군나르 파너벡 알고리즘은 모든 픽셀에 대해 x,y축의 움직임을 감지
            # 계산된 flow에서 최대값이 3 이상이면 움직임이 있다고 판단, check_vision을 False로 변경해 색 탐지를 안하도록 
            if np.max(flow) > 3: #1.5:
                self.check_color = False
                self.get_logger().info(f'Motion Detected!')
            else:
                self.check_color = True
            
            # 이미지 변환 확인용
            if self.img is not None:
                self.get_logger().info("Image successfully converted to OpenCV format")
            else:
                self.get_logger().error("Failed to convert image")
            
            if self.points is None: # 교점 정보가 없으면
                # json 파일이 없으면 
                if not os.path.isfile('/home/capstone2/Go_bot/points.json'):
                    self.get_logger().error(f'Initialize First!')   # 초기화를 하라고 출력
                else:   # json 파일이 있으면
                    # 파일 열어서 self.points에 저장
                    with open('/home/capstone2/Go_bot/points.json', 'r') as jsonfile:
                        self.points = json.load(jsonfile)
            else:   # 교점 정보가 있으면
                if (self.img.size != 0) and self.check_color: # 이미지가 온전하고, 바둑판 위의 움직임이 없으면
                    img_transformed = perspective(self.cornerPoints, self.img)  # 시점변환
                    self.game_state = color_classifier(img_transformed, self.gray, {'device': self.device, 'transform': self.transform, 'model': self.model}, self.points)  # 색 검출
                            
                # self.get_logger().info("state: "+ self.game_state)

            self.prev_gray = self.gray
            
        except Exception as e:
            self.get_logger().error(e)
    
    # 초기화(교점 찾기), 앱에서 대국 시작을 눌렀을 때
    # 서비스 노드
    def initialize_points(self, req, res):
        if req.do_initialize:   # 클라이언트에서 요청이 왔을 때
            img = perspective(self.cornerPoints, self.img)  # 시점 변환
            blur = cv2.GaussianBlur(img, (0, 0), 1)         # 가우시안 블러
            gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)   # grayscale 변환
            canny = cv2.Canny(gray, 35, 40)                 # 캐니 엣지
            
            lines = line_detector(canny)                    # 라인 검출
            self.points = get_points(lines, 30)             # 교점 찾기
           
            self.get_logger().info("Get Points!\n")
            print(self.points)

            # 이미지에 교점을 찍어서 저장 (확인용)
            test_img = img.copy()
            for col in self.points:
                for (x, y) in col:
                    cv2.circle(test_img, (int(x), int(y)), 12, (255, 0, 0), -1)
            cv2.imwrite("/home/capstone2/Go_bot/points.png", test_img)

            # 구한 교점을 json 파일로 저장
            file = '/home/capstone2/Go_bot/points.json'
            with open(file, 'w') as json_file:
                json.dump(self.points, json_file)

            # 요청 응답 작성
            res.done_initialize = True

            return res
        else:
            res.done_initialize = False

            return res
    
    def state_callback(self):
        msg = State()

        # self.game_state는 카메라 입장에서본 상황.
        # 퍼블리시 할때는 사용자 입장에서본 상황을 주고 싶음. -> 문자열을 통째로 뒤집기
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
