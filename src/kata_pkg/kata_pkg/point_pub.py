import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BlackStonePublisher(Node):
    def __init__(self):
        super().__init__('black_stone_publisher')
        self.publisher_ = self.create_publisher(String, 'black_stone_topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        position = input("Enter the black stone position (e.g., D15): ")
        msg = String()
        msg.data = position
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = BlackStonePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
