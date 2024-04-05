import rclpy
from rclpy.node import Node
from baduk_msgs.msg import Go  # 수정 필요: 메시지 유형과 패키지 이름

class GameStateSubscriber(Node):
    def __init__(self):
        super().__init__('game_state_subscriber')
        self.subscription = self.create_subscription(
            Go, 'game_state_topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(
            'Territory: "%s", Winrate: %s, Recommended points: %s, Rate: %s' % (
                msg.territory, msg.winrate, msg.re_point, msg.re_rate))

def main(args=None):
    rclpy.init(args=args)
    node = GameStateSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
