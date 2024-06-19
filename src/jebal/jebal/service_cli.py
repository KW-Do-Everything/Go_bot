import rclpy
from rclpy.node import Node
from baduk_msgs.srv import AddTwoInts

import time

import socket

HOST = '127.0.0.1'  # 서버의 IP 주소
PORT = 8080         # 서버의 포트 번호
message_1 = 'Hello from client'

class SimpleServiceClient(Node):
    def __init__(self):
        super().__init__('simple_service_client')

        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.send_request()

    def send_request(self):
        req = AddTwoInts.Request()
        req.a = 10
        req.b = 20

        self.get_logger().error('Let\'s go.')

        self.future = self.client.call_async(req)
        # self.get_logger().error('jebal')
        # rclpy.spin_until_future_complete(self, self.future)  # 결과를 기다립니다.
        # self.get_logger().error('oh yeah')

        time.sleep(1)
        # TCP 소켓 생성
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # 서버에 연결
            client_socket.connect((HOST, PORT))

            # 서버로 메시지 전송
            client_socket.sendall(message_1.encode())

            # 서버로부터 데이터 받기
            data = client_socket.recv(1024)
            print(f'Received from server: {data.decode()}')

        try:
            response = self.future.result()
            if response is not None:
                self.get_logger().info(f'Result of add_two_ints: {response.sum}')
            else:
                self.get_logger().error('Exception while calling service: %r' % (self.future.exception(),))
        except Exception as e:
            self.get_logger().error('Service call failed: %r' % (e,))

def main(args=None):
    rclpy.init(args=args)
    client = SimpleServiceClient()
    rclpy.spin(client)
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
