import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from baduk_msgs.msg import Go, State# 수정 필요: 메시지 유형과 패키지 이름
from baduk_engine.gtp import gtp  # 수정 필요: gtp 클래스의 위치
from datetime import datetime


class GoGameProcessor(Node):
    def __init__(self):
        super().__init__('solo_play')

        self.kata = gtp()

        self.kata.komi(6.5)

        self.subscriber = self.create_subscription(
            State,
            'game_state',
            self.state_listener_callback,
            10
        ) 

        # self.timer = self.create_timer(0.5, self.timer_callback)

        
        self.publisher_1 = self.create_publisher(Go, 'game_state_topic', 10) # to app
        self.publisher_2 = self.create_publisher(State, 'robot_arm_move_topic', 10) # 로봇팔에 보내야하는 퍼블 리셔 point and flag
        
        self.position = ''
        self.last_state_msg = "." * 361
        self.point = ''
        self.history1 = [""] # 착점 모음1 - all points
        # self.history2 = [" "] # 착점 모음2 - select points

        self.flag = True # 덜어낼지 둘지 정하는 True : place / False : 



#------------------카메라에서 인식된 바둑판 받음 --------------------#

    # def timer_callback(self):
    #     msg1 = State()
    #     if self.position is not None:
    #         msg1.state = self.position
    #         msg1.flag = self.flag
    #         self.publisher_1.publish(msg1)
    #         self.get_logger().info(f'Publishing: "{msg1.state}, flag : {msg1.flag}"')
    #     msg2 = Go()
        

    def state_listener_callback(self, msg):

        if self.last_state_msg != msg.state:

            self.get_logger().info(msg.state)

            #여기다 엔진 비교하는거 추가해야함.
            #비교해서 다르면? -> 다른 상태에 따라서? 엔진엔 있고 카메라에 없다 : 다른 좌표 보내서 덜어내라 명령/ 엔진에 없고 카메라에 있다 : 착수 명령
            # self.kata.check_board() msg.state 랑 비교해서 

            self.flag, self.position = self.diff_to_coordinates(self.kata.check_board(), msg.state) #차이 비교해서 좌표 출력
            self.last_state_msg = msg.state #last_state_msg 업데이트 
            self.get_logger().info(f'Current position: {self.position}, Last history: {self.history1[-1]}, Flag: {self.flag}')


        if (self.position != self.history1[-1]) and (self.flag == True): # 만약 차이 좌표가 이전 히스토리랑 다르고 둬야하는 상황이면,
            self.history1.append(self.position) # 히스토리에 추가하고
            # if(msg.data not in self.history2):
            #     self.history2.append(msg.data)
            
            
            self.kata.place_solo(self.position) # black stone place i want            
            self.get_logger().info('place : %s' %self.position)

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
            
            place_stone = State()

            place_stone.state = self.position #position
            place_stone.flag = self.flag

            self.publisher_1.publish(game_state) # 게임 상태 publishing 
            self.publisher_2.publish(place_stone)





    def diff_to_coordinates(self, str1, str2): # str1 : check_board 엔진 /str2 : msg.state  카메라

        #엔진에 빈칸이고, 카메라에 착수이면 : 들어내야함  : re_flag : False
        #엔진에 점이 있고, 카메라에 빈칸이면 : 바둑 둬야함 : re_flag : True
        if len(str1) != len(str2) or len(str1) != 361: 
            raise ValueError("Strings must be 361 characters long")
        
        re_flag = True
        coordinates_str = ''  # 변경된 위치의 바둑판 좌표를 저장할 문자열

        for i in range(19):
            for j in range(19):
                index = i * 19 + j
                if str1[index] != str2[index]:
                    # 바둑판 좌표는 보통 A1부터 T19까지 (I 제외) 사용합니다.
                    column = chr(j + ord('A') if j < 8 else j + ord('A') + 1)
                    row = str(19 - i)
                    point = column+row
                    coordinates_str += point + " "  # 좌표를 문자열에 추가하고 공백으로 구분
                    if str1[index] == '.' and str2[index] != '.' and point in self.history1:
                        re_flag = False
                        self.history1.remove(point)
                    else:
                        re_flag = True
        return re_flag, coordinates_str.strip()  # 문자열의 끝에 있는 공백을 제거




def main(args=None):
    rclpy.init(args=args)
    node = GoGameProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
