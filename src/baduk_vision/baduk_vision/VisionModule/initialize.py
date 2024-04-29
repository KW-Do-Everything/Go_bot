import cv2
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.neighbors._nearest_centroid import NearestCentroid


def line_detector(canny: np.ndarray) -> np.ndarray: # 타입 헌팅 -> 는 return 값에 대해 씀
    # Hough 변환을 사용하여 선을 감지합니다.
    lines = cv2.HoughLines(canny, 0.5, np.pi/180, 200)

    # 감지된 선의 각도를 MinMaxScaler를 통해 정규화합니다.
    mmss = MinMaxScaler().fit_transform(lines.squeeze()[:,1].reshape(len(lines), 1))

    # DBSCAN 클러스터링을 사용하여 선을 수직과 수평으로 분류합니다.
    cluster_vh = DBSCAN(eps=0.1, min_samples=8).fit(mmss)
    
    # 수직선과 수평선을 저장할 빈 배열을 초기화합니다.
    lines0 = np.empty((0, 2))
    lines1 = np.empty((0, 2))

    # 각 선을 클러스터에 따라 분류합니다.
    for label, line in zip(cluster_vh.labels_, lines):
        if label == 0:
            lines0 = np.append(lines0, line, axis=0)
        elif label == 1:
            lines1 = np.append(lines1, line, axis=0)

    # 각 클러스터의 대표 선을 찾기 위해 AgglomerativeClustering과 NearestCentroid를 사용합니다.
    cluster0 = AgglomerativeClustering(n_clusters=19).fit_predict(lines0)
    cluster1 = AgglomerativeClustering(n_clusters=19).fit_predict(lines1)
    
    '''
    AgglomerativeClustering(n_clusters=19):

n_clusters=19: 군집의 수를 19로 설정합니다. 이 예에서는 바둑판이 19x19 격자임을 고려하여 각 직선 그룹에서 대표적인 19개의 선을 추출하기 위해 사용됩니다.
AgglomerativeClustering은 초기에 각 데이터 포인트를 하나의 군집으로 간주하고, 비슷한 군집끼리 병합해 나가면서 지정된 군집 수에 도달할 때까지 과정을 반복합니다.
.fit_predict(lines0):

fit_predict() 메소드는 군집화 모델을 lines0 데이터에 적합시키고, 각 데이터 포인트가 속한 군집의 레이블을 반환합니다.
lines0은 앞서 HoughLines과 DBSCAN을 통해 추출된 수평선 또는 수직선을 포함하는 배열로, 각 선의 정보는 ρ와 θ 값으로 구성되어 있습니다.
fit_predict를 통해 반환된 cluster0 배열은 lines0의 각 선이 속하는 군집의 인덱스를 담고 있습니다. 이 인덱스는 0부터 18까지의 값을 가질 수 있으며, 각각의 값은 해당 선이 속한 군집을 나타냅니다.
    '''

    # 대표 선의 중심을 계산합니다.
    lines0 = NearestCentroid().fit(lines0, cluster0).centroids_
    lines1 = NearestCentroid().fit(lines1, cluster1).centroids_

    '''
    NearestCentroid():

NearestCentroid 클래스는 주어진 군집의 중심점을 계산하는 알고리즘을 구현합니다. 이 클래스는 각 군집에 대해 중심점을 계산하고, 이 중심점을 통해 새로운 데이터 포인트를 군집화할 때 사용할 수 있습니다.
.fit(lines0, cluster0):

fit 메소드는 lines0 데이터와 cluster0 군집 레이블을 기반으로 모델을 훈련시킵니다. 여기서 lines0은 선들의 ρ와 θ 값으로 이루어진 배열이고, cluster0은 이전에 AgglomerativeClustering을 통해 생성된 군집 레이블입니다.
fit 메소드는 각 군집의 데이터 포인트들을 분석하여 그 중심점을 계산합니다.
.centroids_:

centroids_ 속성은 fit 메소드에 의해 계산된 각 군집의 중심점을 저장합니다. 이 값은 각 군집을 대표하는 선의 ρ와 θ 값을 포함하는 배열입니다.
lines0 = ...는 계산된 중심점을 lines0 변수에 할당합니다. 이를 통해 각 군집의 대표 선이 갱신되며, 이 선들은 바둑판의 격자를 형성하는 데 사용될 수 있습니다.
    
    '''

    # 계산된 중심선을 반환합니다.
    return np.array([lines0, lines1])

def get_points(lines: np.ndarray, threshold: float) -> list: #교차점 찾기
    # 수직선과 수평선을 각각 추출합니다.
    lines0 = lines[0]
    lines1 = lines[1]

    # 교차점을 저장할 빈 배열을 초기화합니다.
    intersectionsF = np.empty((0, 2), np.float32)

    # 모든 수직선과 수평선의 조합에 대해 교차점을 계산합니다.
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

            # 선형 방정식을 풀어 교차점 좌표를 계산합니다.
            x, y = np.linalg.solve(A, b)
            intersectionsF = np.append(intersectionsF, np.array([[x[0], y[0]]]), axis=0)

    # 필터링: 교차점에서 임계값 이내의 점들만 선택합니다.
    points = []
    while len(intersectionsF) > 0:
        remain_points = []
        topLeft = sorted(intersectionsF, key=lambda x: x[0] + x[1])[0]
        topRight = sorted(intersectionsF, key=lambda x: x[0] - x[1])[-1]

        row = []
        x1, y1 = map(int, topLeft)
        x2, y2 = map(int, topRight)

        # 임계값을 사용하여 행에 속하는 점들을 선택합니다.
        for point in intersectionsF:
            x, y = map(int, point)
            dist = abs((x2 - x1) * y - (y2 - y1) * x + (-(x2 - x1) * y1 + (y2 - y1) * x1)) / np.sqrt(
                (x2 - x1) ** 2 + (y2 - y1) ** 2)

            if dist < threshold:
                row.append(point.tolist())
            else:
                remain_points.append(point)

        # 행별 점들을 x 좌표에 따라 정렬합니다.
        points.append(sorted(row, key=lambda x: x[0]))

        intersectionsF = remain_points

    # 최종적으로 모든 교차점을 포함하는 리스트를 반환합니다.
    return points
