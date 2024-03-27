import cv2
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import DBSCAN


def color_classifier(img: np.ndarray, points: list):
    out_img = []

    _, S, V = cv2.split(cv2.cvtColor(cv2.GaussianBlur(img, (0, 0), 3), cv2.COLOR_BGR2HSV))
    for col in points:
        for (x, y) in col:
            pts = [int(x), int(y)]

            s = np.sum(S[pts[1] - 15:pts[1] + 15, pts[0] - 15:pts[0] + 15]) / 15 ** 2
            v = np.sum(V[pts[1] - 15:pts[1] + 15, pts[0] - 15:pts[0] + 15]) / 15 ** 2
            out_img.append([s, v])

    