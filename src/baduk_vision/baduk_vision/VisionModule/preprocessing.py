import cv2
import numpy as np


def CLAHE(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    if len(img.shape) == 3:
        y, cr, cb = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb))
        Y = clahe.apply(y)
        return cv2.cvtColor(cv2.merge((Y, cr, cb)), cv2.COLOR_YCrCb2BGR)
    else:
        return clahe.apply(img)

def perspective(cornerPoints, img):
    topLeft = cornerPoints[0]
    topRight = cornerPoints[1]
    bottomRight = cornerPoints[2]
    bottomLeft = cornerPoints[3]

    w1 = abs(bottomRight[0] - bottomLeft[0])
    w2 = abs(topRight[0] - topLeft[0])
    h1 = abs(topRight[1] - bottomRight[1])
    h2 = abs(topLeft[1] - bottomLeft[1])
    width = int(max([w1, w2]))
    height = int(max([h1, h2]))

    pts = np.float32([[0, 0], [width - 1, 0],
                        [width - 1, height - 1], [0, height - 1]])
    mtrx = cv2.getPerspectiveTransform(cornerPoints, pts)

    return cv2.warpPerspective(img, mtrx, (width, height))