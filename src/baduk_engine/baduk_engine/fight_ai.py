import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from baduk_msgs.msg import Go, State# 수정 필요: 메시지 유형과 패키지 이름
from open_manipulator_msgs.srv import Setarmpos
from baduk_engine.gtp import gtp  # 수정 필요: gtp 클래스의 위치
from datetime import datetime
from baduk_msgs.msg import Vision


class GoGameProcessor(Node):
    def __init__(self):
        super().__init__('fight_ai')

        self.kata = gtp()

        # self.kata.komi(6.5)

        self.subscriber = self.create_subscription(
            State,
            'game_state',
            self.state_listener_callback,
            10
        ) 

        self.subscriber2 = self.create_subscription(
            Vision,
            'check_vision',
            self.vision_listener_callback,
            10
        )
        
        self.vision_check = True # 움직일 때 :false, 멈추면 true
        self.mv_sign = False

        # self.timer = self.create_timer(0.5, self.timer_callback)

        
        self.publisher_1 = self.create_publisher(Go, 'game_state_topic', 10) # to app
        # self.publisher_2 = self.create_publisher(State, 'robot_arm_move_topic', 10) # 로봇팔에 보내야하는 퍼블 리셔 point and flag
        
        self.position = ''
        self.last_state_msg = "." * 81
        self.point = ''
        self.history1 = [""] # 착점 모음1 - all points
        self.flag = True # 덜어낼지 둘지 정하는 True : place / False : 
        
        
        self.arm_client = self.create_client(Setarmpos, 'set_arm_position') # 여기 클라이언트 생성함,
        while not self.arm_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Arm service not available, waiting again...') # 생성 실패시 오류코드


    def send_arm_position(self, position, m_position): #바둑돌 좌표 보내는 서비스
        req = Setarmpos.Request()
        req.stone_position = position #좌표 업데이트
        req.minus_stone_position = m_position
        future = self.arm_client.call_async(req) 
        future.add_done_callback(self.handle_arm_response)


    def handle_arm_response(self, future):
        try:
            response = future.result()
            if response.arm_move_flag: #true면 = 로봇팔이 다 움직였으면,
                self.get_logger().info(f'Arm successfully moved to {future.result().arm_move_flag} and returned.') # 서비스에서 리턴 받는거 출력
                # self.get_logger().info(f'Arm successfully moved to and returned.')
            else:
                self.get_logger().info('Arm movement failed or did not return to position.')
        except Exception as e:
            self.get_logger().error('Service call failed %r' % e)


    def vision_listener_callback(self, msg2):
        # 움직일 때 :false, 멈추면 true

        if msg2.check_vision == True and self.vision_check == False: # 움직이다가 멈추면,
            self.mv_sign = True  # 엔진 실행하는 사인
            return True
        else:
            self.mv_sign = False # 엔진 멈춰 있으라는 사인
            return False
        # self.vision_check = msg2.check_vision
        # self.get_logger().info("vision_check : " + str(self.vision_check))
        # self.get_logger().info("check_vision : " + str(msg2.check_vision))
        # self.get_logger().info("mv_sign : " + str(self.mv_sign))


    def state_listener_callback(self, msg):
        if len(msg.state) != 81:
            self.get_logger().warn(f'Received game state with invalid length: {len(msg.state)} characters. Expected 81 characters.')
            return  # 이 경우 함수를 안전하게 종료
        
        self.get_logger().info('last: ' + self.last_state_msg)
        self.get_logger().info('msg: ' + msg.state)

        if self.last_state_msg != msg.state: # 새로 입력 받으면,

            # self.get_logger().info(msg.state)
            # self.get_logger().info(self.last_state_msg)

            self.black_input_point = self.point_update_by_diff(self.last_state_msg, msg.state) #차이로 좌표 뽑아내서
            
            # self.get_logger().info("black_input_point : " + self.black_input_point)

            # if self.black_input_point not in self.history1:
            self.kata.place_black(self.black_input_point) #검정 돌 엔진에 보내고,
            self.history1.append(self.black_input_point) #히스토리에 업데이트


            white_point = self.kata.play_white() # ai 가 생성 한 뒤, 
            self.history1.append(white_point) #히스토리에 업데이트 한 다음
            self.get_logger().info(" white_point" + white_point)

            tmp = msg.state
            updated_state = self.update_board_state_by_point(tmp, white_point, 'w') # ai가 둔 곳을 msg.state에 업데이트
            self.flag, self.position = self.diff_to_coordinates(self.kata.check_board(), updated_state) # 들어낸 좌표를 추출
            for c in self.position:
                updated_state = self.update_board_state_by_point(updated_state, c, '.')
            self.get_logger().info("들어낼 좌표:")
            for i in range(len(self.position)):
                self.get_logger().info(self.position[i])
            self.last_state_msg = updated_state #last_state_msg 업데이트 

            # white_point 좌표 는 로봇 팔로 보내야 함.



            #이부분에 로봇팔 움직이는 토픽 발행

            # place_stone = State()
            # place_stone.state = white_point #position
            # place_stone.flag = True # 두기
            # self.publisher_2.publish(place_stone)
            self.send_arm_position(white_point, self.position) # true : 두기 ######################여기서 흰돌 좌표 tele한테 보냄

            # 다 움직였다면

            # self.get_logger().info("mv : " + str(self.mv_sign))
            # self.subscriber2
            # while(not self.vision_listener_callback):
            #     self.get_logger().info("mv : " + str(self.mv_sign))
            #     pass

            #앱에 상태 업데이트

            game_state = Go()

            game_state.territory = self.kata.final_score()
            game_state.winrate = [self.kata.white_win_rate(), 10000-self.kata.white_win_rate()]
            analyze_result = self.kata.analyze()
            try:
                game_state.re_point = [analyze_result[i] for i in range(0, 10, 2)]
                game_state.re_rate = [analyze_result[i] for i in range(1, 10, 2)]
            except:
                game_state.re_point = [analyze_result[i] for i in range(0, len(analyze_result), 2)]
                game_state.re_rate = [analyze_result[i] for i in range(1, len(analyze_result), 2)]


            self.get_logger().info(
                'territory: "%s", winrate: %s, re_point: %s, re_rate: %s' % (
                game_state.territory,
                game_state.winrate,  # 배열이나 리스트도 문자열로 자동 변환됩니다.
                game_state.re_point,
                game_state.re_rate
                )
            )

            self.publisher_1.publish(game_state) # 게임 상태 publishing 보내고,


            

            # tmp = msg.state
            # updated_state = self.update_board_state_by_point(tmp, white_point, 'w')
            
            # self.get_logger().info("msg.state : " + msg.state)
            # self.get_logger().info("tmp : " + tmp)
            # self.get_logger().info("last_state_msg old: " + self.last_state_msg) 

            # self.flag, self.position = self.diff_to_coordinates(self.kata.check_board(), tmp) #차이 비교해서 좌표 출력 / 차이 좌표 여러개 나올 수 있음
        #     self.flag, self.position = self.diff_to_coordinates(self.kata.check_board(), updated_state)

        #     if (self.flag == False): #들어내야하면
        #         # place_stone2 = State()
        #         for extract in self.position:
        #             # place_stone2.state = extract #position
        #             # place_stone2.flag = False
                    
        #             updated_state = self.update_board_state_by_point(updated_state, extract, '.')   # 돌이 빠진 보드 업데이트
        #             if extract != white_point:
        #                 self.send_arm_position(extract,False) #들어내라 시킴
        #                 while( not self.vision_listener_callback):  # 로봇팔이 다 움직일때까지 대기
        #                     self.get_logger().info('대기중...')
        #                     pass
        #     else : # 차이가 없으면.
        #         pass # 넘어감

        #     self.last_state_msg = updated_state #last_state_msg 업데이트 
        #     # self.get_logger().info("last_state_msg update : " + self.last_state_msg) 

        # else:
        #     pass




    def point_update_by_diff(self, str1, str2):
        if len(str1) != len(str2) or len(str1) != 81: 
            raise ValueError("Strings must be 81 characters long")
        
        re_flag = True
        coordinates_str = ''  # 변경된 위치의 바둑판 좌표를 저장할 문자열

        for i in range(9):
            for j in range(9):
                index = i * 9 + j
                if str1[index] != str2[index]:
                    # 바둑판 좌표는 보통 A1부터 T19까지 (I 제외) 사용합니다.
                    column = chr(j + ord('A') if j < 8 else j + ord('A') + 1)
                    row = str(9 - i)
                    point = column+row
                    if point not in self.history1:
                        return point
                    

    def update_board_state_by_point(self, str1, point, stone='w'):
        if len(str1) != 81:
            raise ValueError("Strings must be 81 characters long")

        # 좌표 파싱: 예를 들어 'H8'이면, 열은 'H', 행은 '8'
        column = ord(point[0].upper()) - ord('A')
        if point[0].upper() > 'I':  # 'I'를 건너뛰는 경우
            column -= 1
        row = 9 - int(point[1:])

        # 문자열 인덱스 계산
        index = row * 9 + column

        # 문자열을 리스트로 변환하여 특정 위치 수정
        str_list = list(str1)
        str_list[index] = stone  # 'b', 'w', 또는 '.'를 사용하여 상태 업데이트
        
        self.get_logger().info("str_list : " + ''.join(str_list)) 


        # 리스트를 다시 문자열로 변환
        return ''.join(str_list)





    def diff_to_coordinates(self, str1, str2): # str1 : check_board 엔진 /str2 : msg.state  카메라

        #엔진에 빈칸이고, 카메라에 착수이면 : 들어내야함  : re_flag : False
        #엔진에 점이 있고, 카메라에 빈칸이면 : 바둑 둬야함 : re_flag : True
        if len(str1) != len(str2) or len(str1) != 81: 
            raise ValueError("Strings must be 81 characters long")
        
        re_flag = True
        coordinates_str = [] # 변경된 위치의 바둑판 좌표를 저장할 리스트

        for i in range(9):
            for j in range(9):
                index = i * 9 + j
                if str1[index] != str2[index]:
                    column = chr(j + ord('A') if j < 8 else j + ord('A') + 1)
                    row = str(9 - i)
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
