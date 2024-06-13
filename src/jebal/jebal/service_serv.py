import rclpy
from rclpy.node import Node
from baduk_msgs.srv import AddTwoInts  # Change this to your package and service file
import time

class AddTwoIntsServer(Node):

    def __init__(self):
        super().__init__('add_two_ints_server')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        
        self.client = self.create_client(AddTwoInts, 'add_two_ints2')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')


    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Incoming request: a={request.a}, b={request.b}. Sum={response.sum}")
        time.sleep(5)
        self.send_request()
        self.get_logger().info(f"Incoming request: a={request.a}, b={request.b}. Sum={response.sum}")
        return response

    def send_request(self):
        req = AddTwoInts.Request()
        req.a = 20
        req.b = 30
        self.future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, self.future)  # 결과를 기다립니다.
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
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
