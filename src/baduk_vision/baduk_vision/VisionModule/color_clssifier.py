import cv2
import numpy as np
import torch
from PIL import Image as PILImage

from baduk_vision.baduk_vision.VisionModule.preprocessing import perspective


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
    cv2.imwrite("/home/capstone/Go_bot/testImg.jpg", img)
    
    game_state = ""
    for col in points:
        for (x, y) in col:

            x1 = max(0, x - 15)
            y1 = max(0, y - 15)
            x2 = min(img.shape[1], x + 16) 
            y2 = min(img.shape[0], y + 16)

            cropped = gray[int(y1):int(y2), int(x1):int(x2)]
            
            image = PILImage.fromarray(cropped)
            image = torch_utils['transform'](image).unsqueeze(0)

            image = image.to(torch_utils['device'])

            with torch.no_grad():
                outputs = torch_utils['model'](image)
                
            output = outputs[0][0].item()

            if output < 0.5:
                if np.mean(cropped) > 150:
                    game_state += "w"
                else:
                    game_state += "b"
            else:
                game_state += '.'

    return game_state

    