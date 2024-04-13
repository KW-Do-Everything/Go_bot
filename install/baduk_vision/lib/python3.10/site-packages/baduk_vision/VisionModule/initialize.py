import cv2
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.neighbors._nearest_centroid import NearestCentroid


def line_detector(canny: np.ndarray) -> np.ndarray:

    lines = cv2.HoughLines(canny, 0.5, np.pi/180, 100)

    # 수직/수평선 구분
    #cluster_vh = KMeans(n_clusters=2).fit(lines.squeeze()[:, 1].reshape(len(lines), 1))
    mmss = MinMaxScaler().fit_transform(lines.squeeze()[:,1].reshape(len(lines), 1))
    cluster_vh = DBSCAN(eps=0.1, min_samples=8).fit(mmss)
    
    lines0 = np.empty((0, 2))
    lines1 = np.empty((0, 2))
    for label, line in zip(cluster_vh.labels_, lines):
        if label == 0:
            lines0 = np.append(lines0, line, axis=0)
        elif label == 1:
            lines1 = np.append(lines1, line, axis=0)

    cluster0 = AgglomerativeClustering(n_clusters=19).fit_predict(lines0)
    cluster1 = AgglomerativeClustering(n_clusters=19).fit_predict(lines1)

    lines0 = NearestCentroid().fit(lines0, cluster0).centroids_
    lines1 = NearestCentroid().fit(lines1, cluster1).centroids_

    return np.array([lines0, lines1])

def get_points(lines: np.ndarray, threshold: float) -> list:
    lines0 = lines[0]
    lines1 = lines[1]

    intersectionsF = np.empty((0, 2), np.float32)
    for rho1, theta1 in lines0:
        for rho2, theta2 in lines1:
            A = np.array([
                [np.cos(theta1), np.sin(theta1)],
                [np.cos(theta2), np.sin(theta2)]
            ])

            b = np.array([
                [rho1],
                [rho2]
            ])

            x, y = np.linalg.solve(A, b)
            intersectionsF = np.append(intersectionsF, np.array([[x[0], y[0]]]), axis=0)

    '''for circle in circle_points:
        intersectionsF = np.append(intersectionsF, [circle[:-1]], axis=0)'''
    
    points = []
    while len(intersectionsF) > 0:
        remain_points = []
        topLeft = sorted(intersectionsF, key=lambda x: x[0] + x[1])[0]
        topRight = sorted(intersectionsF, key=lambda x: x[0] - x[1])[-1]

        row = []
        x1, y1 = map(int, topLeft)
        x2, y2 = map(int, topRight)

        for point in intersectionsF:

            x, y = map(int, point)

            dist = abs((x2 - x1) * y - (y2 - y1) * x + (-(x2 - x1) * y1 + (y2 - y1) * x1)) / np.sqrt(
                (x2 - x1) ** 2 + (y2 - y1) ** 2)

            if dist < threshold:
                row.append(point.tolist())
            else:
                remain_points.append(point)
        """
        # 한줄에 19개의 점이 검출되었는지 확인
        tmp = []
        check = [False for i in range(len(row))]
        if len(row) > 19:

            for i in range(len(row) - 1):
                if not check[i]:
                    tmp.append(row[i])
                for j in range(i + 1, len(row)):
                    dist = np.sqrt((row[i][0] - row[j][0]) ** 2 + (row[i][1] - row[j][1]) ** 2)
                    if dist < mean_radius:
                        check[j] = True
            row = tmp
        """
        points.append(sorted(row, key=lambda x: x[0]))

        intersectionsF = remain_points
    #return points
    return points