import cv2
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.neighbors._nearest_centroid import NearestCentroid


def line_detector(canny: np.ndarray) -> np.ndarray:
    """
    입력
        canny: 캐니 엣지 영상
    출력
        np.ndarray: 수직 수평선 각 19개씩
    """

    # 허프 변환
    lines = cv2.HoughLines(canny, 0.5, np.pi/180, 200)

    # 수직/수평선 구분
    # MinMaxScaler로 정규화 후 DBSCAN으로 군집화해서 직선을 각도를 기준으로 두 그룹으로 나눔
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

    # 각도를 기준으로 나눈 선들 사이에서 19개씩 그룹을 만듦.
    cluster0 = AgglomerativeClustering(n_clusters=19).fit_predict(lines0)
    cluster1 = AgglomerativeClustering(n_clusters=19).fit_predict(lines1)

    lines0 = NearestCentroid().fit(lines0, cluster0).centroids_
    lines1 = NearestCentroid().fit(lines1, cluster1).centroids_

    return np.array([lines0, lines1])

def get_points(lines: np.ndarray, threshold: float) -> list:
    """
    입력
        lines: line_detector 결과
        threshold: 직선과 점사이의 거리 threshold
    출력
        points: list, 교점 361개, 우상단->우하단까지 정렬한 결과
    """

    # 수직/수평선 DBSCAN의 결과가 계속 바뀌므로 어떤게 수직인지 수평인지 모름
    lines0 = lines[0]
    lines1 = lines[1]

    # 선형대수 내용
    # 두 변수와 두 식이 있을때 Matrix로 만들어 풀기
    # cos(t1)*x + sin(t1)*y = r1
    # cos(t2)*x + sin(t2)*y = r2
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
    
    # 교점 정렬
    # max(x+y)인 점이 좌 상단, min(x-y)인 점이 우 상단
    # 좌상 - 우상 선을 이어서 이 직선과 교점들의 거리를 비교, threshold보다 작으면 row에 추가
    # row를 x좌표 기준으로 정렬후 최종 결과인 points에 추가 후 원래 리스트에서 삭제
    # 원래 리스트의 길이가 0이 되면 끝
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
    return points