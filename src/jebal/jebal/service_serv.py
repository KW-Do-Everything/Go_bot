import rclpy
from rclpy.node import Node
from baduk_msgs.srv import AddTwoInts  # Change this to your package and service file
import time

import socket

HOST = '127.0.0.1'   # 서버의 IP 주소
PORT = 8080         # 서버의 포트 번호



class AddTwoIntsServer(Node):

    def __init__(self):
        super().__init__('add_two_ints_server')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        
        # self.client = self.create_client(AddTwoInts, 'add_two_ints2')
        # while not self.client.wait_for_service(timeout_sec=1.0):
        #     self.get_logger().info('Service not available, waiting again...')


    def add_two_ints_callback(self, request, response):
        # TCP 소켓 생성
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # 소켓을 특정 IP 주소와 포트에 바인딩
            server_socket.bind((HOST, PORT))
            
            # 클라이언트의 연결 요청을 기다림
            server_socket.listen()

            print(f'Server is listening on {HOST}:{PORT}')

            # 클라이언트 연결 수락
            conn, addr = server_socket.accept()
            with conn:
                print(f'Connected by {addr}')

                while True:
                    # 클라이언트로부터 데이터 받기
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f'Received data: {data.decode()}')

                    # 클라이언트에게 데이터 전송
                    conn.sendall(b'Hello from server')

                print('Connection closed by client')

        

        response.sum = request.a + request.b
        self.get_logger().info(f"Incoming request: a={request.a}, b={request.b}. Sum={response.sum}")
        time.sleep(5)
        self.get_logger().info(f"Incoming request: a={request.a}, b={request.b}. Sum={response.sum}")

        

        # self.send_request()
        # self.get_logger().info(f"Incoming request: a={request.a}, b={request.b}. Sum={response.sum}")
        return response

    # def send_request(self):
    #     req = AddTwoInts.Request()
    #     req.a = 20
    #     req.b = 30
    #     self.get_logger().error('Let\'s go.')

    #     self.future = self.client.call_async(req)

    #     self.get_logger().error('jebal')
        
    #     rclpy.spin_until_future_complete(self, self.future)  # 결과를 기다립니다.

    #     self.get_logger().error('oh yeah')
    #     try:
    #         response = self.future.result()
    #         if response is not None:
    #             self.get_logger().info(f'Result of add_two_ints: {response.sum}')
    #         else:
    #             self.get_logger().error('Exception while calling service: %r' % (self.future.exception(),))
    #     except Exception as e:
    #         self.get_logger().error('Service call failed: %r' % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
