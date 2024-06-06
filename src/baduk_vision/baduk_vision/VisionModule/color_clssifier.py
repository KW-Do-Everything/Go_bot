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
    cropped = cv2.resize(cropped, (224, 224))  # 이미지를 고정된 크기로 리사이즈
    cropped = cropped / 255.0

    return index, cropped

from torch.cuda.amp import autocast

def color_classifier(img: np.ndarray, model, points: list) -> str:
    img_list = []
    game_state = ""

    cv2.imwrite("/home/capstone2/Go_bot/testImg.jpg", img)

    # 전처리 병렬화
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(preprocess_image, img, x, y, i * len(col) + j)
                   for i, col in enumerate(points)
                   for j, (x, y) in enumerate(col)]

        for future in concurrent.futures.as_completed(futures):
            index, cropped = future.result()
            img_list.append((index, cropped))

    # 인덱스를 기준으로 정렬
    img_list.sort(key=lambda x: x[0])
    img_batch = np.array([img for _, img in img_list], dtype=np.float32)

    # 모델 예측
    with torch.no_grad():
        img_batch_tensor = torch.tensor(img_batch).permute(0, 3, 1, 2).float().to("cuda")  # Change to tensor and permute to match model input
        with autocast():
            predictions = model(img_batch_tensor)

    # 예측 결과 처리
    for prediction in predictions:
        cls = prediction.probs.top1
        if cls == 0:
            game_state += 'b'
        elif cls == 1:
            game_state += 'w'
        else:
            game_state += '.'

    if len(game_state) != 361:
        raise ValueError("Game state length is not 361")

    return game_state
