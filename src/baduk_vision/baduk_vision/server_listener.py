import rclpy as rp
from rclpy.node import Node
from baduk_msgs.srv import Initialize
from baduk_msgs.msg import Finish

from baduk_vision.robotInfo import url4listener, robot_num

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class ServerListener(Node):

    def __init__(self):
        super().__init__('server_listener')

        self.start = True
        self.listenerClient = self.create_client(Initialize, 'do_initialize')
        self.req = Initialize.Request()

        self.finish_pub = self.create_publisher(
            Finish,
            'finish',
            10
        )
        self.init_firebase()

    # Firebase 초기화
    def init_firebase(self):
        cred = credentials.Certificate("/home/capstone/Go_bot/src/baduk_vision/app-for-baduk-robot-5vzlm0-firebase-adminsdk-k8czr-3f94cbab09.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': url4listener
        })
        ref_baduk = db.reference('Robots/'+robot_num+'/baduk/init')
        ref_baduk.listen(self.baduk_listener)

        ref_baduk_finish = db.reference('Robots/'+robot_num+'/baduk/finish')
        ref_baduk_finish.listen(self.baduk_finish_listener)


        ref_othello = db.reference('Robots/'+robot_num+'/othello/init')
        ref_othello.listen(self.othello_listener)

        ref_othello_finish = db.reference('Robots/'+robot_num+'/othello/finish')
        ref_othello_finish.listen(self.othello_finish_listener)
    
    # Firebase Listener
    # 실시간 데이터베이스에 변경점이 있으면 감지하는 함수
    def baduk_listener(self, event):
        if self.start == True:
            self.get_logger().info(f'Firebase data changed: {event.data}')
            try:
                # 앱에서 대국시작 버튼을 누르면 초기화(교점 찾기) 서비스 요청
                if event.data == True:
                    self.send_request()
                    self.start = False
            except:
                self.get_logger().error("Error: Failed to Get 'init' data")
        else:
            self.get_logger().info(f'Firebase data changed: {event.data}')
            # 앱에서 대국종료 버튼을 누르면 start변수 False로 바꾸기
            if event.data == False:
                self.start = True

    def baduk_finish_listener(self, event):
        self.get_logger().info(f'Firebase data changed: {event.data}')
        try:
            if event.data == True:
                self.finish_request()
        except:
            self.get_logger().error("Error: Failed to Get 'finish' data")

    def othello_listener(self, event):
        if self.start == True:
            self.get_logger().info(f'Firebase data changed: {event.data}')
            try:
                # 앱에서 대국시작 버튼을 누르면 초기화(교점 찾기) 서비스 요청
                if event.data == True:
                    self.send_request()
                    self.start = False
            except:
                self.get_logger().error("Error: Failed to Get 'init' data")
        else:
            self.get_logger().info(f'Firebase data changed: {event.data}')
            # 앱에서 대국종료 버튼을 누르면 start변수 False로 바꾸기
            if event.data == False:
                self.start = True

    def othello_finish_listener(self, event):
        self.get_logger().info(f'Firebase data changed: {event.data}')
        try:
            if event.data == True:
                self.finish_request()
        except:
            self.get_logger().error("Error: Failed to Get 'finish' data")


    # 서비스 서버 노드 (초기화(교점 찾기)하라고 명령)
    def send_request(self):
        self.get_logger().info(f'send Request!!')
        self.req.do_initialize = True
        self.future = self.listenerClient.call_async(self.req)

    # AI reset하라고 명령
    def finish_request(self):
        self.get_logger().info(f'send Finish Request!!')
        msg = Finish()
        msg.finish = True
        self.finish_pub.publish(msg)


def main(args=None):
    rp.init(args=args)
    service_client = ServerListener()
    rp.spin(service_client)
    service_client.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()
        