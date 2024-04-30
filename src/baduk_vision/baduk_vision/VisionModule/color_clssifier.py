import cv2
import numpy as np
import torch
from PIL import Image as PILImage


def color_classifier(img: np.ndarray, gray: np.ndarray, torch_utils, points: list) -> str:
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
    cv2.imwrite("/home/capstone2/Go_bot/testImg.jpg", img)
    
    game_state = ""
    for col in points:
        for (x, y) in col:
            
            # 교점 주위로 이미지 crop
            x1 = max(0, x - 20)
            y1 = max(0, y - 20)
            x2 = min(img.shape[1], x + 21) 
            y2 = min(img.shape[0], y + 21)

            cropped = gray[int(y1):int(y2), int(x1):int(x2)]
            
            # PIL 이미지로 변환 후 transform 적용, device에 올리기
            image = PILImage.fromarray(cropped)
            image = torch_utils['transform'](image).unsqueeze(0)
            image = image.to(torch_utils['device'])

            with torch.no_grad():
                outputs = torch_utils['model'](image)   # 모델로 crop 이미지 추정 (1: 비어있는 곳(격자), 0: 돌이 있는 곳)
                
            output = outputs[0][0].item()   # outputs: tensor([[1.]], device='cuda:0') -> 확률만 output에 취함

            if output < 0.5:    # 빈 곳일 확률이 50% 이하면
                if np.mean(cropped) > 150:  # gray 이미지 픽셀의 평균으로 흑/백 돌 구분 
                    game_state += "w"
                else:
                    game_state += "b"
            else:   # 빈 곳일 확률이 50% 이상
                game_state += '.'

    return game_state

    