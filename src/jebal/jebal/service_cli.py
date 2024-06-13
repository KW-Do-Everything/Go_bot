import rclpy
from rclpy.node import Node
from baduk_msgs.srv import AddTwoInts

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
    client = SimpleServiceClient()
    rclpy.spin(client)
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
