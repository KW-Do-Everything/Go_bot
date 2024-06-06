import cv2
import numpy as np
import torch
from PIL import Image as PILImage
import concurrent.futures

def preprocess_image(img, x, y, index):
    x1 = max(0, x - 20)
    y1 = max(0, y - 20)
    x2 = min(img.shape[1], x + 21)
    y2 = min(img.shape[0], y + 21)

    cropped = img[int(y1):int(y2), int(x1):int(x2)]
    cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

    return index, cropped

def color_classifier(img: np.ndarray, model, points: list) -> str:
    """
    입력
        img: perspective transform된 입력 영상
        points: 바둑판 교점 좌표
    출력
        game_state: str 81자리 문자열
    """

    # 확인용 이미지 저장
    cv2.imwrite("/home/capstone2/Go_bot/testImg.jpg", img)

    img_list = []
    game_state = ""
    tasks = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, col in enumerate(points):
            for j, (x, y) in enumerate(col):
                index = i * len(col) + j
                futures.append(executor.submit(preprocess_image, img, x, y, index))

        for future in concurrent.futures.as_completed(futures):
            index, cropped = future.result()
            img_list.append((index, cropped))

    # 인덱스를 기준으로 정렬
    img_list.sort(key=lambda x: x[0])
    img_batch = [img for _, img in img_list]
    
    #v8
    # 모델 예측
    with torch.no_grad():
        predictions = model.predict(img_batch)

    # 예측 결과 처리
    for prediction in  predictions:
        cls = prediction.probs.data.argmax()
        if cls == 0:
            game_state += 'b'
        elif cls == 1:
            game_state += 'w'
        else:
            game_state += '.'

    if len(game_state) != 81:
        raise ValueError("Game state length is not 81")
    
    print(game_state)

    return game_state
