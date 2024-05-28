import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from baduk_msgs.msg import State

class BlackStonePublisher(Node):
    def __init__(self):
        super().__init__('black_stone_publisher')
        self.publisher_ = self.create_publisher(String, 'black_stone_topic', 10)
        
        self.last_state_msg = "." * 361
        self.subscriber = self.create_subscription(
            State,
            'game_state',
            self.state_listener_callback,
            10
        )
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.position = None



    def timer_callback(self):
        msg = String()
        if self.position is not None:
            msg.data = self.position
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing: "{msg.data}"')

    def state_listener_callback(self, msg):
        if self.last_state_msg != msg.state:
            self.get_logger().info(msg.state)
            self.position = self.diff_to_coordinates(self.last_state_msg, msg.state)
            self.last_state_msg = msg.state



    def diff_to_coordinates(self, str1, str2):
        if len(str1) != len(str2) or len(str1) != 361:
            raise ValueError("Strings must be 361 characters long")
        coordinates_str = ''  # 변경된 위치의 바둑판 좌표를 저장할 문자열
        for i in range(19):
            for j in range(19):
                index = i * 19 + j
                if str1[index] != str2[index] and str1[index] == '.':
                    # 바둑판 좌표는 보통 A1부터 T19까지 (I 제외) 사용합니다.
                    column = chr(j + ord('A') if j < 8 else j + ord('A') + 1)
                    row = str(19 - i)
                    coordinates_str += column + row + " "  # 좌표를 문자열에 추가하고 공백으로 구분
        return coordinates_str.strip()  # 문자열의 끝에 있는 공백을 제거





def main(args=None):
    rclpy.init(args=args)
    node = BlackStonePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
