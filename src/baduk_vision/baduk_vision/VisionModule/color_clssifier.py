import cv2
import numpy as np
import torch
from PIL import Image as PILImage
import matplotlib.pyplot as plt


def color_classifier(img: np.ndarray, gray: np.ndarray, model, points: list) -> str:
    """
    입력
        img: perspective transform된 입력 영상
        gray: img의 grayscale
        torch_utils: {device, transform, model} (dict)
        points: 바둑판 교점 좌표
    출력
        game_state: str 361자리 문자열
    """

    # 확인용 이미지 저장
    # cv2.im write("/home/capstone2/Go_bot/testImg.jpg", img)

    # fig = plt.figure(figsize=(30, 50))
    # idx = 361

    img_list = []
    game_state = ""
    for i, col in enumerate(points):
        for j, (x, y) in enumerate(col):
            
            # 교점 주위로 이미지 crop
            x1 = max(0, x - 20)
            y1 = max(0, y - 20)
            x2 = min(img.shape[1], x + 21) 
            y2 = min(img.shape[0], y + 21)

            cropped = img[int(y1):int(y2), int(x1):int(x2)]
            cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
            img_list.append(PILImage.fromarray(cropped))

            # ax = fig.add_subplot(19, 19, idx)
            # image = PILImage.fromarray(cropped)
            # ax.imshow(image)
            # ax.axis('off')
            # idx -= 1

    # fig.savefig('./test.png')
    with torch.no_grad():
        predictions = model.predict(img_list)
    for prediction in predictions:
        if prediction.probs.data.argmax() == 0:
            game_state += 'b'
        elif prediction.probs.data.argmax() == 1:
            game_state += 'w'
        else:
            game_state += '.'

    return game_state

    