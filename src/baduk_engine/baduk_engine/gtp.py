import subprocess
from time import sleep
import time
import threading
import re
import numpy as np

from datetime import datetime
import select




# 예외처리는 수정해야함


#있어야 하는 기능
'''
1. 현재 상황에서의 추천 수 lz-analyze 나 kata-analyze로 필요할 때 받아옴 
2. 현재 상황에서 승률 -> kata-raw-nn의 whiteWin 사용
3. 현재 집 차이 -> final_score OR kata-raw-nn의 whiteLead 의 평균과 비교해봐야함,
'''



# 실행할 외부 프로그램의 경로
exe_path = '/home/capstone1/kata/katago'
# 외부 프로그램에 전달할 인자, 예를 들어 'gtp' 명령어 
args = ['gtp', '-model', '/home/capstone1/kata/kata.gz']

#### 뒤에 cfg 옵션 나중에 설정해야함####




class gtp():
    def __init__(self):
        self.process=subprocess.Popen([exe_path] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print("test")
        self.history=[]
        # print("set history")


######################## 다른 함수에 쓸 read, write 함수 #########

    # 원하는 문자열 시작과 끝 줄 정해서 읽기
    """ 
    def read_analysis_output(self):
        output = []
        capture = False
        while True:
            line = self.process.stdout.readline().decode('utf-8')
            if not line:
                break  # EOF

            if "Controller: lz-genmove_analyze" in line:
                capture = True  # 시작 지점 감지
                output.append(line.strip())
                print("one")
            elif capture:
                output.append(line.strip())
                print("two")
                if line.startswith('play'):
                    break  # 종료 지점 감지

        # 출력된 결과를 분석하고 싶은 형태로 가공
        analysis_data = '\n'.join(output)
        return analysis_data
        
    """
#########****************************************************###############
    def write(self, txt):
        try:
            # 문자열을 UTF-8 바이트 문자열로 인코딩
            txt_bytes = (txt + "\n").encode('utf-8')
            self.process.stdin.write(txt_bytes)
            self.process.stdin.flush()
        except Exception as e:
            print("Error while writing to stdin\n" + str(e))

            
    def readline(self): # 일반적인 한줄 짜리 return 받을 때 사용
        answer=self.process.stdout.readline().decode("utf-8")
        while answer in ("\n","\r\n","\r"):
            answer=self.process.stdout.readline().decode("utf-8")
        return answer
    
    def readlines(self): # kata-raw-nn 에 사용
        lines = []
        t = 0
        while True:
            line = self.process.stdout.readline().decode("utf-8")
            lines.append(line.strip())  # strip()을 사용하여 문자열의 앞뒤 공백 제거
            if t > 1: #한뭉텅이 출력
                break
            t += 1
        return lines
    
    def read_from_to(self, start, end): 
        lines = []
        capture = False
        while True:
            line = self.process.stdout.readline().decode("utf-8")
            # print("line")
            if str(start) in line:
                lines.append(line.strip())  # strip()을 사용하여 문자열의 앞뒤 공백 제거
                capture = True
            elif capture:  # 조건 충족 시 반복 중지

                if str(end) in line:
                    break
                lines.append(line.strip())  # strip()을 사용하여 문자열의 앞뒤 공백 제거
        return lines
    
    def read_equal2question(self):
        return self.read_from_to("=","? unknown command")
        

            
#########****************************************************###############

######### 기본 제공 gtp 함수들 //// 한줄짜리 리턴, 형식 : "= ~" ########

	####hight level function####
    def boardsize(self,size=19):
        self.size=size
        self.write("boardsize "+str(size))
        # print("why")
        answer=self.readline()
        if answer[0]=="=":
            # print("hi")
            return True
        else:return False
		
    def reset(self):
        self.write("clear_board")
        answer=self.readline()
        if answer[0]=="=":return True
        else:return False

    def komi(self,k): # 덤 설정
        self.write("komi "+str(k))
        answer=self.readline()
        if answer[0]=="=":
            self.komi_value=k
            return True
        else:
            self.komi_value=0
            return False

    def place_black(self,move): # 좌표에 검은돌 두기
        if move == "RESIGN":
            print("WARNING: trying to play RESIGN as GTP move")
            self.history.append(["b",move])
            return True
        self.write("play black "+move)
        answer=self.readline()
        if answer[0]=="=":
            self.history.append(["b",move])
            return True
        else:return False	
	
    def place_white(self,move): # 좌표에 흰돌 두기
        if move == "RESIGN":
            print("WARNING: trying to play RESIGN as GTP move")
            self.history.append(["w",move])
            return True
        self.write("play white "+move)
        answer=self.readline()
        if answer[0]=="=":
            self.history.append(["w",move])
            return True
        else:return False


    def play_black(self): # 검은돌 둬주기 
        self.write("genmove black")
        answer=self.readline().strip()
        try:
            move=answer.split(" ")[1].upper()
            self.history.append(["b",move])
            return move
        except Exception as e:
            raise print("GRPException in genmove_black()\nanswer='"+answer+"'\n"+str(e))

		
    def play_white(self): # 흰돌 둬주기
        self.write("genmove white")
        answer=self.readline().strip()
        try:
            move=answer.split(" ")[1].upper()
            self.history.append(["w",move])
            return move
        except Exception as e:
            raise print("GRPException in genmove_white()\nanswer='"+answer+"'\n"+str(e))


    def undo(self): # 되돌리기
        self.reset()
        self.komi(self.komi_value)
        try:
			#adding handicap stones
            if len(self.free_handicap_stones)>0:
                self.set_free_handicap(self.free_handicap_stones)
            self.history.pop()
            history=self.history[:]
            self.history=[]
            for color,move in history:
                if color=="b":
                    if not self.place_black(move):
                        return False
                else:
                    if not self.place_white(move):
                        return False
            return True			
        except Exception as e:
            raise print("GRPException in undo()\n"+str(e))
	
    def place(self,move,color): # 좌표에 원하는 돌 두기
        if color==1:
            return self.place_black(move)
        else:
            return self.place_white(move)
	
    def name(self): # 엔진 이름 출력
        self.write("name")
        answer=self.readline().strip()
        try:
            return " ".join(answer.split(" ")[1:])
        except Exception as e:
            raise print("GRPException in name()\nanswer='"+answer+"'\n"+str(e))
	
    def version(self): # 엔진 버전 출력
        self.write("version")
        answer=self.readline().strip()
        try:
            return answer.split(" ")[1]
        except Exception as e:
            raise print("GRPException in version()\nanswer='"+answer+"'\n"+str(e))


    def set_free_handicap(self,positions): # 원하는 곳에 수 깔기
        self.free_handicap_stones=positions[:]
        stones=""
        for p in positions:
            stones+=p+" "
        self.write("set_free_handicap "+stones.strip())
        answer=self.readline().strip()
        try:
            if answer[0]=="=":
                return True
            else:
                return False	
        except Exception as e:
            raise print("GRPException in set_free_handicap()\nanswer='"+answer+"'\n"+str(e))
	
    def undo_standard(self): # 되돌리기
        self.write("undo")
        answer=self.readline()
        try:
            if answer[0]=="=":
                return True
            else:
                return False			
        except Exception as e:
            raise print("GRPException in undo()\nanswer='"+answer+"'\n"+str(e))
	 

	
	#is that needed?
    def final_score(self): # 계가
        self.write("final_score")
        answer=self.readline().strip()
        return " ".join(answer.split(" ")[1:])
    
	
    
	#is that needed?
    def final_status(self,move):
        self.write("final_status "+move)
        answer=self.readline()
        answer=answer.strip()
        return " ".join(answer.split(" ")[1:])

    def set_time(self,main_time=30,byo_yomi_time=30,byo_yomi_stones=1): # 초읽기 세팅
        self.write("time_settings "+str(main_time)+" "+str(byo_yomi_time)+" "+str(byo_yomi_stones))
        answer=self.readline()
        try:
            if answer[0]=="=":return True
            else:return False
        except Exception as e:
            raise print("GRPException in set_time()\nanswer='"+answer+"'\n"+str(e))

    def quit(self): # 나가기
        self.write("quit")
        answer=self.readline()
        if answer[0]=="=":return True
        else:return False	

    def terminate(self):
        t=10
        while 1:
            self.quitting_thread.join(0.0)	
            if not self.quitting_thread.is_alive():
                print("The bot has quitted properly")
                break
            elif t==0:
                print("The bot is still running...")
                print("Forcefully closing it now!")
                break
            t-=1
            print("Waiting for the bot to close",t,"s")
            sleep(1)
		
        try: self.process.kill()
        except: pass
        try: self.process.stdin.close()
        except: pass


    def close(self):
        print("Now closing")
        self.quit()


    def save_sgf(self):
        current_date = datetime.now().strftime('%Y%m%d')
        self.write("printsgf " + current_date + ".sgf")
        answer=self.readline()
        if answer[0]=="=":return True
        else:return False	





    ############ katago 고유함수, 두줄 이상 출력, 출력 형식은 "="으로 시작해서 "? unknown command"가 나올줄까지 #####
        
    def lz_analyze(self,color, time, min, max = None): # 현재 상태에서의 추천 수
        # analyzes = []
        self.write("lz-analyze " + str(color) + " " + str(time) + " maxmoves " + str(min))
        answer = self.readlines()
        # analyzes.append(answer[2])
        info_list = answer[2].split(" info ")
        info_list = ["info " + move_info if i > 0 else move_info for i, move_info in enumerate(info_list)]
        self.write("\n")
        return info_list
    
    def kata_analyze(self,color, time, min, max = None): # 현재 상태에서의 추천 수
        # analyzes = []
        self.write("kata-analyze " + str(color) + " " + str(time) + " maxmoves " + str(min))
        answer = self.readlines()
        # analyzes.append(answer[2])
        info_list = answer[2].split(" info ")
        info_list = ["info " + move_info if i > 0 else move_info for i, move_info in enumerate(info_list)]
        self.write("\n")
        output = []
        for i in info_list:
            i.split(" ")[3]

        return info_list
    
    def analyze(self):
        tmp = []
        output = []
        list = self.lz_analyze("b", 50 , 5)
        for i in list:
            # print(i)
            tmp = i.split(" ")
            # print(tmp[2], tmp[6])
            output.append(tmp[2])
            output.append(tmp[6])
        return output



    def lz_genmove_analyze(self):
        self.write("lz-genmove_analyze")
        self.write(".")
        answer=self.read_equal2question()
        return answer

    def kata_genmove_analyze(self):
        self.write("kata-genmove_analyze")
        answer=self.read_output_lines()
        return answer
    


    
    def genmove(self, color):
        self.write("genmove " + str(color))
        answer = self.readline().strip()
        answer = answer.split(" ")[1]
        return answer

    def genmove_debug(self, color):
        self.write("genmove_debug " + str(color))
        self.write(".")
        answer=self.read_equal2question()
        return answer



    def showboard(self):
        self.write("showboard")
        self.write(".")
        answer = self.read_equal2question()
        return answer

    def kata_raw_nn(self, num):
        self.write("kata-raw-nn " + str(num))
        self.write(".")
        answer = self.read_equal2question()
        return answer
    
    def white_win_rate(self):
        winrates =[]
        t = 0
        while True:
            tmp0 = self.kata_raw_nn(t)[1]
            # print(type(tmp0))
            winrates.append(tmp0.split(" ")[1])
            t += 1
            if(t > 7):
                break
        winrates_numeric = [float(value) for value in winrates]
        winrate = np.mean(winrates_numeric)
        return int(winrate*10000)

    def white_lead(self):
        leads =[]
        t = 0
        while True:
            tmp0 = self.kata_raw_nn(t)[4]
            # print(tmp0)
            leads.append(tmp0.split(" ")[1])

            t += 1
            if(t > 7):
                break
        white_lead_numeric = [float(value) for value in leads]
        print(white_lead_numeric)
        lead = np.mean(white_lead_numeric)
        return lead
    

    ################################
    def testdragon(self, num):
        if self.boardsize(19):
            print("Board size set to 19x19")
        if self.komi(6.5):
            print("Komi set to 6.5")
        print("name : ", self.name())

        i =0
        while(i < num):
            i +=1
            print(self.genmove("w"))
            print(self.genmove("b"))
        data = dict( territory = self.final_score(), winRate = [self.white_win_rate(), 10000-self.white_win_rate()],  recommend = self.analyze())
        self.close()
        return data



#혼자두기 

    def place_solo(self, point):
        if len(self.history) % 2  == 0: # black stone
            self.write("play black "+point)
            answer=self.readline()
            if answer[0]=="=":
                self.history.append(["b",point])
                return True
            else:return False
        else: # white stone
            self.write("play white "+point)
            answer=self.readline()
            if answer[0]=="=":
                self.history.append(["w",point])
                return True
            else:return False
    



    ## 바둑판 현황 체크
    def check_board(self):
        board_lines = self.showboard()[1:21]

        board_size = len(board_lines) - 1  # 제목 행을 제외한 실제 바둑판 크기
        board_string = ""

        # 바둑판의 각 행을 순회
        for line in board_lines[1:]:  # 첫 번째 행(열 제목)을 제외
            for char in line:  # 첫 번째 열(행 제목)을 제외
                if char == '.':
                    board_string += '.'  # 빈 칸
                elif char == 'X':
                    board_string += 'b'  # 검은 돌
                elif char == 'O':
                    board_string += 'w'  # 흰 돌

        return board_string





'''
    def place_white(self,move): # 좌표에 흰돌 두기
        if move == "RESIGN":
            print("WARNING: trying to play RESIGN as GTP move")
            self.history.append(["w",move])
            return True
        self.write("play white "+move)
        answer=self.readline()
        if answer[0]=="=":
            self.history.append(["w",move])
            return True
        else:return False



'''




# 메인 함수에서 클래스를 사용하여 KataGo와의 상호작용을 시작합니다.
def main():
    # KataGo 실행 파일, 모델 파일, 설정 파일 경로
    # katago_path = '~/kata_test/katago'
    # model_path = '~/kata_test/KataGo6b.gz'
    # config_path = '~/kata_test/config.cfg'
    
    # gtp 클래스 인스턴스 생성
    kata = gtp()
    print("setting on")
    # 19x19 바둑판 설정
    if kata.boardsize(19):
        print("Board size set to 19x19")
    
    # 덤 설정
    if kata.komi(6.5):
        print("Komi set to 6.5")

    # 이름 확인



    # (D16) 위치에 검은 돌 두기
    # if kata.place_black(('D16')):
    #     print("Black stone placed at (D16)")
    

    # i =0
    # while(i < 5):
    #     i +=1
    #     print(kata.genmove("w"))
    #     # print(kata.lz_analyze( "b", 50 , 5))
    #     print(kata.genmove("b"))


    # #있는 기보 불러와서 확인 
    # kata.write("loadsgf 5half.sgf")
    # print(kata.showboard())

    # #현재 바둑판 출력
    # tmp = kata.showboard()
    # tmp2 = '\n'.join(tmp)
    # print(tmp2)

    # print("계가 : ", kata.final_score())
    # print("백 승률 : ",kata.white_win_rate())
    # print("백 lead : ",kata.white_lead())
    
    # #현재 년월일을 이름으로 기보 저장
    # if kata.save_sgf():
    #     print("sgf save")

    # data = dict( territory = kata.final_score(), winRate = [kata.white_win_rate(), 10000-kata.white_win_rate()],  recommend = kata.analyze())
    # print(data)
    # print(data['territory'])
    # print(data["winRate"][1])

    # print(kata.showboard()[1:21])
    # kata.place_white(('E15'))
    # print(kata.showboard()[1:21])
    # kata.place_black(('D4'))


    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    # print(kata.showboard()[1:21])
    # kata.play_white()
    # print(kata.showboard()[1:21])
    # kata.play_black()
    i = 0
    while i < 5:
        kata.play_black()
        print(kata.showboard()[1:21])
        kata.play_white()
        print(kata.showboard()[1:21])
        i +=1
    i = 0
    while i < 5:
        kata.play_black()
        print(kata.check_board())
        kata.play_white()
        print(kata.check_board())
        i +=1


    # 사용 후 자원 정리
    kata.close()

if __name__ == "__main__":
    main()