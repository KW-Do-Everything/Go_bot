import cv2

# 좌표를 저장할 리스트
points = []

# 마우스 콜백 함수
def mouse_callback(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 클릭 시
        if len(points) < 4:  # 네 개의 좌표까지만 저장
            points.append((x, y))
            print(f"Point {len(points)}: ({x}, {y})")

        if len(points) == 4:
            print("4 points have been selected:", points)
            cv2.destroyAllWindows()  # 창 닫기

# 웹캠 설정
webcam = cv2.VideoCapture(0)  # 웹캠 번호 설정 (0, 1, 2 등으로 변경 가능)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 프레임 너비 설정
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)  # 프레임 높이 설정

cv2.namedWindow("Webcam")  # 창 이름 설정
cv2.setMouseCallback("Webcam", mouse_callback)  # 마우스 콜백 함수 등록

while True:
    # 웹캠으로부터 프레임 읽기
    ret, frame = webcam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 현재 프레임을 화면에 표시
    cv2.imshow("Webcam", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 네 개의 점을 선택하면 루프를 종료
    if len(points) == 4:
        break

# 리소스 해제
webcam.release()
cv2.destroyAllWindows()

# 선택된 좌표 출력
print("Selected Points:", points)
