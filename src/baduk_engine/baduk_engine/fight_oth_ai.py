import rclpy
from rclpy.node import Node
# from std_msgs.msg import String
from baduk_msgs.msg import Othello, State, Finish# 수정 필요: 메시지 유형과 패키지 이름s
from baduk_engine.gtp_o import gtp  # 수정 필요: gtp 클래스의 위치
from datetime import datetime
from baduk_msgs.msg import Vision, PointOth


class OthelloGameProcessor(Node):
    def __init__(self):
        super().__init__('fight_oth_ai')

        self.kata = gtp()

        self.subscriber = self.create_subscription( # 데이터 
            State,
            'othello_state',
            self.state_listener_callback,
            10
        ) 

        # self.subscriber2 = self.create_subscription( # 비전데이터를 받을지 확인
        #     Vision,
        #     'check_vision',
        #     self.vision_listener_callback,
        #     10
        # )

        # self.subscriber3 = self.create_subscription( # 끝남을 확인
        #     Finish,
        #     'finish',
        #     self.finish_listener_callback,
        #     10
        # )
        
        self.vision_check = True # 움직일 때 :false, 멈추면 true
        self.mv_sign = False

        self.publisher_1 = self.create_publisher(Othello, 'game_state_topic', 10) # 앱에다 보내는 토픽
        self.point_topic = self.create_publisher(PointOth, 'Point_topic', 10) # 바둑돌 둘 토픽

        self.position = ''
        self.last_state_msg = "...........................wb......bw..........................."
        self.point = ''
        self.history1 = [""] # 착점 모음1 - all points
        self.flag = True # 덜어낼지 둘지 정하는 True : place / False : 
        self.finish = False


    # def finish_listener_callback(self, msg3):
    #     if msg3.finish:
    #         self.kata.reset()
    #         self.finish = False
    #         self.history1 = []
    #         self.get_logger().info("Finish!!!!!!!")


    # def vision_listener_callback(self, msg2):
    #     # 움직일 때 :false, 멈추면 true

    #     if msg2.check_vision == True and self.vision_check == False: # 움직이다가 멈추면,
    #         self.mv_sign = True  # 엔진 실행하는 사인
    #         return True
    #     else:
    #         self.mv_sign = False # 엔진 멈춰 있으라는 사인
    #         return False


    def state_listener_callback(self, msg):
        if len(msg.state) != 64:
            self.get_logger().warn(f'Received game state with invalid length: {len(msg.state)} characters. Expected 64 characters.')
            return  # 이 경우 함수를 안전하게 종료 - 확인해야함
        
        self.get_logger().info(msg.state)

        if self.last_state_msg != msg.state: # 카메라에서 새로 입력 받으면,
            self.get_logger().info("new state")
            self.get_logger().info("engine state : " + self.kata.check_board())

            self.black_input_point = self.point_update_by_diff(self.kata.check_board(), msg.state) #엔진과 비전의 차이로 흑돌의 좌표 뽑아내서
            
            # self.get_logger().error("type error" + str(type(self.black_input_point)) + str(self.black_input_point)) ## 오류를 찾아서 출력

            if self.black_input_point == '':
                return 
            
            self.get_logger().info(" black stone place at : "+ self.black_input_point)

            self.kata.place_black(self.black_input_point) #검정 돌 엔진에 보내고,
            # self.history1.append(self.black_input_point) #히스토리에 업데이트
            self.get_logger().info("engine state : " + self.kata.check_board())

            white_point = self.kata.play_white() # ai 가 생성 한 뒤, 
            # self.history1.append(white_point) #히스토리에 업데이트 한 다음
            self.get_logger().info("white_point " + white_point)
            self.get_logger().info("engine state : " + self.kata.check_board())
            # if self.is_valid_go_position(white_point): # 만약 이상한돌이면 초기화
            #     self.get_logger().info("Good Point!")
            # else:
            #     self.kata.reset()
            #     self.history1 = []
            #     game_state2 = Go()
            #     game_state2.finish = True
            #     self.publisher_1.publish(game_state2) # 초기화 해야해
            #     self.get_logger().error("Oh yeah! game set")
            #     return


            tmp = msg.state # msg.state 는 비전에서 받아온 상태
            # self.get_logger().info(tmp)

            updated_state = self.update_board_state_by_point(tmp, white_point, 'w') # tmp 에 ai가 둔 곳을 msg.state에 업데이트
            self.position = self.diff_to_coordinates(self.kata.check_board(), updated_state) # 뒤집을 좌표를 추출
            # for c in self.position:
            #     self.history1.remove(c) #따낼 좌표를 history 에서 삭제
            # self.get_logger().info("들어낼 좌표:")
            # for i in range(len(self.position)): ############################################################
            #     self.get_logger().info(self.position[i])


            self.last_state_msg = self.kata.check_board() # 엔진으로부터 last_state_msg 업데이트 

            # white_point 좌표 는 로봇 팔로 보내야 함.

            point_co = PointOth()
            point_co.stone_position = white_point # 둘 좌표
            point_co.reverse_stone_position = self.position # 뒤집을 좌표



            #이부분에 로봇팔 움직이는 토픽 발행

            self.point_topic.publish(point_co) # 두고 뺄 좌표 토픽 발행

            # 다 움직였다면

            #앱에 상태 업데이트

            empty_count, black_count = self.get_board_stats(self.last_state_msg)
            self.get_logger().info("empty_count" + str(empty_count))
            self.get_logger().info("black_count" + str(black_count))

            game_state = Othello()

            game_state.re_point = self.kata.reg_genmove("black")
            game_state.stone_num = str(black_count)
            game_state.empty = str(empty_count)




            # if white_point == "PASS":
            #     self.finish = True
            # game_state.finish = self.finish


            self.get_logger().info(
                'recommand: "%s", stone_num: %s, empty: %s' % (
                game_state.re_point,
                game_state.stone_num,  # 배열이나 리스트도 문자열로 자동 변환됩니다.
                game_state.empty
                )
            )
            # game_state.game = 'othello'
            self.publisher_1.publish(game_state) # 게임 상태 publishing 보내고,



            # if self.finish == True:
            #     self.kata.reset()
            #     self.finish = False
            #     self.history1 = []


    # def is_valid_go_position(self, position): # 들어온 좌표가 유효한지 확인
    #     # 유효한 좌표는 A1~T19, I를 제외합니다.
    #     if len(position) < 2 or len(position) > 3:
    #         return False

    #     column = position[0].upper()
    #     row = position[1:]

    #     if column in 'I':
    #         return False  # 'I'는 바둑판에서 사용하지 않습니다.
        
    #     if column < 'A' or column > 'T':
    #         return False  # 'A'에서 'T' 범위를 벗어납니다 (단, 'I' 제외).

    #     if not row.isdigit():
    #         return False  # 행 숫자가 아니면 유효하지 않습니다.
        
    #     row_number = int(row)
    #     if row_number < 1 or row_number > 19:
    #         return False  # 1에서 19 범위를 벗어납니다.

    #     return True
    
    def get_board_stats(self, board_state):
        """
        현재 보드 상태에서 남은 빈칸 수와 흑돌의 수를 반환하는 함수
        
        :param board_state: 현재 보드 상태 문자열 (64자: '.' 빈칸, 'X' 흑돌, 'O' 백돌)
        :return: (empty_count, black_count) 남은 빈칸 수와 흑돌의 수
        """
        empty_count = board_state.count('.')  # 빈칸은 '.'로 표시됨
        black_count = board_state.count('b')  # 흑돌은 'X'로 표시됨
        return empty_count, black_count





    def point_update_by_diff(self,  engine_state, camera_state):
        """
        카메라에서 들어온 상태와 엔진 상태를 비교하여 새로 추가된 돌의 좌표를 반환.

        :param engine_state: AI 엔진의 보드 상태 (64자 문자열, '.'은 빈칸, 'X'는 흑돌, 'O'는 백돌)
        :param camera_state: 카메라에서 받은 실제 보드 상태 (64자 문자열, '.'은 빈칸, 'X'는 흑돌, 'O'는 백돌)
        :return: 새로 추가된 돌의 좌표 문자열 (예: "A1")
        """
        if len(engine_state) != 64 or len(camera_state) != 64:
            raise ValueError("engine_state와 camera_state는 모두 64자 길이여야 합니다.")
        
        columns = 'ABCDEFGH'
        new_stone_position = ''

        for i in range(64):
            # 엔진 상태와 카메라 상태가 다르고, 엔진에는 없지만 카메라에 돌이 있는 경우 새로운 돌로 간주
            if engine_state[i] == '.' and camera_state[i] in ('w', 'b'):
                row = (i // 8) +1 # 행 계산 (1에서 8까지)
                column = columns[i % 8]  # 열 계산 (A에서 H까지)
                new_stone_position = f"{column}{row}"
                break  # 새 돌을 찾았으면 종료
        
        return new_stone_position

                    

    def update_board_state_by_point(self, board_state, point, stone='X'):
        """
        주어진 좌표에 돌을 두고 보드 상태를 업데이트하는 함수.
        
        :param board_state: 현재 보드 상태를 나타내는 문자열 (64자, '.'은 빈칸, 'X'는 흑돌, 'O'는 백돌)
        :param point: 돌을 두는 좌표 (예: "D3")
        :param stone: 놓을 돌의 종류 ('X' 또는 'O', 기본값은 'X')
        :return: 업데이트된 보드 상태 문자열
        """
        
        if len(board_state) != 64:
            raise ValueError("board_state는 64자 길이여야 합니다.")
        
        # 좌표 파싱 (예: 'D3' -> 열: D, 행: 3)
        column = point[0].upper()
        row = point[1]

        # 열과 행을 인덱스로 변환
        columns = 'ABCDEFGH'
        try:
            col_index = columns.index(column)
            row_index = 8 - int(row)
        except ValueError:
            raise ValueError("잘못된 좌표 형식입니다. A1~H8 사이의 좌표를 입력해야 합니다.")

        # 1차원 문자열 인덱스로 변환
        index = row_index * 8 + col_index

        # 문자열을 리스트로 변환하여 특정 위치 수정
        board_list = list(board_state)
        board_list[index] = stone  # 흑돌('X') 또는 백돌('O') 추가

        # 리스트를 다시 문자열로 변환
        return ''.join(board_list)






    def diff_to_coordinates(self, engine_state, camera_state):
        """
        인공지능 상태와 카메라 상태를 비교하여 뒤집어야 할 돌의 좌표를 반환합니다.
        
        :param engine_state: 인공지능에서 관리하는 상태 문자열 (64자, '.'은 빈칸, 'X'는 흑돌, 'O'는 백돌)
        :param camera_state: 카메라에서 감지된 현재 보드 상태 문자열 (64자)
        :return: 뒤집어야 할 돌의 좌표 리스트 (예: ['C3', 'D4'])
        """

        if len(engine_state) != 64 or len(camera_state) != 64:
            raise ValueError("두 상태 모두 64자 길이여야 합니다.")

        flipped_coordinates = []  # 뒤집힌 돌의 좌표를 저장할 리스트
        columns = 'ABCDEFGH'

        # 각 좌표를 비교하여 돌이 뒤집힌 부분을 찾음
        for i in range(64):
            if engine_state[i] != camera_state[i] and engine_state[i] != '.':
                # 좌표를 (A1 ~ H8) 형식으로 변환
                x = i % 8
                y = (i // 8) +1 # 8x8 보드이므로 행은 위에서 아래로 계산
                coordinate = f"{columns[x]}{y}"
                flipped_coordinates.append(coordinate)

        return flipped_coordinates





def main(args=None):
    rclpy.init(args=args)
    node = OthelloGameProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
