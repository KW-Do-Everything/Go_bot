import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from baduk_msgs.msg import Go  # 수정 필요: 메시지 유형과 패키지 이름
from my_first_package.gtp import gtp  # 수정 필요: gtp 클래스의 위치

class GoGameProcessor(Node):
    def __init__(self):
        super().__init__('go_game_processor')
        self.subscription = self.create_subscription(
            String, 'black_stone_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Go, 'game_state_topic', 10)
        self.kata = gtp()

    def listener_callback(self, msg):
        black_position = msg.data
        self.kata.place_black(black_position)
        white_position = self.kata.play_white()
        self.get_logger().info('gen_White : %s' % white_position)
        game_state = Go()

        game_state.territory = self.kata.final_score()
        game_state.winrate = [self.kata.white_win_rate(), 10000-self.kata.white_win_rate()]
        analyze_result = self.kata.analyze()
        game_state.re_point = [analyze_result[i] for i in range(0, 10, 2)]
        game_state.re_rate = [analyze_result[i] for i in range(1, 10, 2)]


        self.get_logger().info(
            'territory: "%s", winrate: %s, re_point: %s, re_rate: %s' % (
            game_state.territory,
            game_state.winrate,  # 배열이나 리스트도 문자열로 자동 변환됩니다.
            game_state.re_point,
            game_state.re_rate
            )
        )
        self.publisher_.publish(game_state)


def main(args=None):
    rclpy.init(args=args)
    node = GoGameProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
