import rclpy as rp
from rclpy.node import Node
from baduk_msgs.srv import Initialize

from baduk_vision.robotInfo import url, robot_num

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class ServerListener(Node):

    def __init__(self):
        super().__init__('server_listener')

        self.start = 0
        self.listenerClient = self.create_client(Initialize, 'do_initialize')
        self.req = Initialize.Request()
        self.init_firebase()

    def init_firebase(self):
        cred = credentials.Certificate("/home/capstone/Go_bot/src/baduk_vision/app-for-baduk-robot-5vzlm0-firebase-adminsdk-k8czr-3f94cbab09.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://app-for-baduk-robot-5vzlm0-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        ref = db.reference('Robots/'+robot_num)
        ref.listen(self.firebase_listener)
        
    def firebase_listener(self, event):
        if self.start != 0:
            self.get_logger().info(f'Firebase data changed: {event.data}')
            try:
                if event.data['init'] == True:
                    self.send_request()
            except:
                print("error")
        self.start = 1

    def send_request(self):
        self.get_logger().info(f'send Request!!')
        self.req.do_initialize = True
        self.future = self.listenerClient.call_async(self.req)


def main(args=None):
    rp.init(args=args)
    service_client = ServerListener()
    rp.spin(service_client)
    service_client.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()
        