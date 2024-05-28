import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from baduk_msgs.msg import Go, State# 수정 필요: 메시지 유형과 패키지 이름
from baduk_engine.gtp import gtp  # 수정 필요: gtp 클래스의 위치
from datetime import datetime


class GoGameProcessor(Node):
    def __init__(self):
        super().__init__('fight_ai')

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
        self.flag = True # 덜어낼지 둘지 정하는 True : place / False : 


    def state_listener_callback(self, msg):

        if self.last_state_msg != msg.state: # 새로 입력 받으면,

            self.get_logger().info(msg.state) 

            self.black_input_point = self.point_update_by_diff(self.last_state_msg, msg.state) #차이로 좌표 뽑아내서
            

            # if self.black_input_point not in self.history1:
            self.kata.place_black(self.black_input_point) #검정 돌 엔진에 보내고,
            self.history1.append(self.black_input_point) #히스토리에 업데이트


            white_point = self.kata.play_white() # ai 가 생성 한 뒤, 
            self.history1.append(white_point) #히스토리에 업데이트 한 다음

            # white_point 좌표 는 로봇 팔로 보내야 함.

            #이부분에 로봇팔 움직이는 토픽 발행

            place_stone = State()

            place_stone.state = white_point #position
            place_stone.flag = True

            self.publisher_2.publish(place_stone)

            # 다 움직였다면

            #앱에 상태 업데이트

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

            self.publisher_1.publish(game_state) # 게임 상태 publishing 보내고,





            self.flag, self.position = self.diff_to_coordinates(self.kata.check_board(), msg.state) #차이 비교해서 좌표 출력 / 차이 좌표 여러개 나올 수 있음

            if (self.flag == False): #들어내야하면
                place_stone2 = State()
                for extract in self.position.split():
                    place_stone2.state = extract #position
                    place_stone2.flag = False

                    self.publisher_2.publish(place_stone2)
            else : # 차이가 없으면.
                #넘어감
                pass

            self.last_state_msg = msg.state #last_state_msg 업데이트 ?????????????????????/


    def point_update_by_diff(self, str1, str2):
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
                    if point not in self.history1:
                        return point





    def diff_to_coordinates(self, str1, str2): # str1 : check_board 엔진 /str2 : msg.state  카메라

        #엔진에 빈칸이고, 카메라에 착수이면 : 들어내야함  : re_flag : False
        #엔진에 점이 있고, 카메라에 빈칸이면 : 바둑 둬야함 : re_flag : True
        if len(str1) != len(str2) or len(str1) != 361: 
            raise ValueError("Strings must be 361 characters long")
        
        re_flag = True
        coordinates_str = [] # 변경된 위치의 바둑판 좌표를 저장할 리스트

        for i in range(19):
            for j in range(19):
                index = i * 19 + j
                if str1[index] != str2[index]:
                    # 바둑판 좌표는 보통 A1부터 T19까지 (I 제외) 사용합니다.
                    column = chr(j + ord('A') if j < 8 else j + ord('A') + 1)
                    row = str(19 - i)
                    point = column+row
                    coordinates_str.append(point)  # 좌표를 문자열에 추가하고 공백으로 구분
                    if str1[index] == '.' and str2[index] != '.':
                        re_flag = False
                    else:
                        re_flag = True
        return re_flag, coordinates_str  # 문자열의 끝에 있는 공백을 제거




def main(args=None):
    rclpy.init(args=args)
    node = GoGameProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
