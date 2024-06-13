import rclpy
from rclpy.node import Node
from baduk_msgs.srv import AddTwoInts  # Change this to your package and service file
import time

class AddTwoIntsServer(Node):

    def __init__(self):
        super().__init__('add_two_ints_server2')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints2', self.add_two_ints_callback)
        

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Incoming request: a={request.a}, b={request.b}. Sum={response.sum}")
        time.sleep(5)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
