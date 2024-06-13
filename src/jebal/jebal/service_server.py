import rclpy
from rclpy.node import Node
from baduk_msgs.srv import Square  # 변경: 여러분의 패키지명으로 수정

class SquareService(Node):
    def __init__(self):
        super().__init__('square_service')
        self.srv = self.create_service(Square, 'square', self.square_callback)

    def square_callback(self, request, response):
        response.square = request.number ** 2
        self.get_logger().info(f'Received: {request.number}, Squared: {response.square}')
        return response

def main(args=None):
    rclpy.init(args=args)
    square_service = SquareService()
    rclpy.spin(square_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
