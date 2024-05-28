import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from baduk_msgs.msg import Go  # 수정 필요: 메시지 유형과 패키지 이름
from jebal.gtp import gtp  # 수정 필요: gtp 클래스의 위치
from datetime import datetime

class GoGameProcessor(Node):
    def __init__(self):
        super().__init__('solo_play')
        self.kata = gtp()
        self.kata.komi(6.5)

        self.subscription = self.create_subscription(
            String, 'black_stone_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Go, 'game_state_topic', 10)

        self.point = ''
        self.history1 = [" "] # 착점 모음1 - all points
        # self.history2 = [" "] # 착점 모음2 - select points

        self.flag = True



    def listener_callback(self, msg):
        if (msg.data != self.history1[-1]):
            self.history1.append(msg.data)
            # if(msg.data not in self.history2):
            #     self.history2.append(msg.data)
            
            
            self.kata.place_solo(msg.data) # black stone place i want            
            self.get_logger().info('place : %s' %msg.data)

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
            # self.kata.showboard()
            self.publisher_.publish(game_state)


def main(args=None):
    rclpy.init(args=args)
    node = GoGameProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
