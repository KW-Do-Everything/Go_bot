import cv2
import numpy as np
import cupy as cp

def CLAHE(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    if len(img.shape) == 3:
        # 이미지가 컬러인 경우 LAB 색공간으로 변환 
        l, a, b = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2LAB))
        # L 채널에 대해 CLAHE 적용
        L = clahe.apply(l) # 밝기에 clahe 적용
        # 변환된 L 채널과 원래의 a, b 채널을 합쳐서 색상 보정
        return cv2.cvtColor(cv2.merge((L, a, b)), cv2.COLOR_LAB2BGR)
    else:
        # 이미지가 그레이스케일인 경우 바로 CLAHE 적용
        return clahe.apply(img)
'''
    
CLAHE (Contrast Limited Adaptive Histogram Equalization)는 
이미지의 대비를 개선하기 위해 사용되는 고급 히스토그램 평활화 기법입니다.
 기본적인 히스토그램 평활화(Histogram Equalization)가 전체 이미지에 걸쳐 밝기의 분포를 균일하게 만드는 반면, 
 CLAHE는 지역적인 대비를 개선하여 이미지의 세부적인 부분까지 보다 명확하게 만들어 줍니다.

 클립 리밋(Clip Limit):
클립 리밋은 대비 제한의 정도를 정의하며, 
이 값이 높을수록 각 타일에서의 히스토그램 평활화가 강하게 적용됩니다. 
적절한 클립 리밋 값 설정은 대비 개선과 노이즈 증가 사이의 균형을 결정하는 데 중요한 역할을 합니다.

'''

'''
L (Lightness): 밝기를 나타내며, 0에서 100 사이의 값을 가집니다. 0은 완전한 검정, 100은 완전한 백색을 의미합니다.
A (Green-Red axis): 색상 성분 중 녹색에서 빨간색으로의 범위를 나타냅니다. 음수 값은 녹색을, 양수 값은 빨간색을 나타냅니다.
B (Blue-Yellow axis): 색상 성분 중 파란색에서 노란색으로의 범위를 나타냅니다. 음수 값은 파란색을, 양수 값은 노란색을 나타냅니다.


'''


def HE(img):
    if len(img.shape) == 3:
        # 이미지가 컬러인 경우 YUV 색공간으로 변환
        y, u, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2YUV))
        # Y 채널(밝기)에 대해 히스토그램 평활화 적용
        Y = cv2.equalizeHist(y)
        # 평활화된 Y 채널과 원래의 U, V 채널을 합쳐서 색상 보정
        return cv2.cvtColor(cv2.merge((Y, u, v)), cv2.COLOR_YUV2BGR)
    else:
        # 이미지가 그레이스케일인 경우 바로 히스토그램 평활화 적용
        return cv2.equalizeHist(img)



def perspective(cornerPoints, img):
    topLeft, topRight, bottomRight, bottomLeft = cornerPoints
    w1 = abs(bottomRight[0] - bottomLeft[0])
    w2 = abs(topRight[0] - topLeft[0])
    h1 = abs(topRight[1] - bottomRight[1])
    h2 = abs(topLeft[1] - bottomLeft[1])
    width = int(max(w1, w2))
    height = int(max(h1, h2))

    # 목표 좌표 지정
    pts = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
    mtrx = cv2.getPerspectiveTransform(cornerPoints, pts)

    # 투시 변환 적용
    return cv2.warpPerspective(img, mtrx, (width, height))


def homomorphic_filter(img):
    # 여러 단계의 처리를 거쳐 조명과 반사를 분리하고 이미지 대비를 개선하는 필터 적용
    # 중요한 처리 단계를 강조하고 기술적인 설명 추가

    img_YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y = img_YUV[:, :, 0]

    y_gpu = cp.asarray(y)
    rows = y_gpu.shape[0]
    cols = y_gpu.shape[1]

    # illumination elements와 reflectance elements를 분리하기 위해 log 취하기
    imgLog = cp.log1p(cp.array(y, dtype='float') / 255) # y를 0-1 사이로 만든뒤 log

    # frequency를 이미지로 나타내면 4분면에 대칭으로 나타남
    # 4분면중 하나에 이미지를 대응시키기위해 row, col을 두배
    M = 2 * rows + 1
    N = 2 * cols + 1

    # 가우시안 마스크 생성 sigma=10
    sigma=10
    (X, Y) = cp.meshgrid(cp.linspace(0, N-1, N), cp.linspace(0, M-1, M))
    Xc = cp.ceil(N/2)
    Yc = cp.ceil(M/2)

    gaussianNumerator = (X - Xc)**2 + (Y - Yc)**2

    # LPF와 HPF
    LPF = cp.exp(-gaussianNumerator / (2*sigma*sigma))
    HPF = 1 - LPF

    LPF_shift = cp.fft.ifftshift(LPF.copy())
    HPF_shift = cp.fft.ifftshift(HPF.copy())

    img_FFT = cp.fft.fft2(imgLog.copy(), (M, N))
    img_LF = cp.real(np.fft.ifft2(img_FFT.copy() * LPF_shift, (M, N)))
    img_HF = cp.real(np.fft.ifft2(img_FFT.copy() * HPF_shift, (M, N)))

    gamma1 = 0.3
    gamma2 = 1.5
    img_adjusting = gamma1 * img_LF[0:rows, 0:cols] + gamma2 * img_HF[0:rows, 0:cols]

    img_exp = cp.expm1(img_adjusting)
    img_exp = (img_exp - cp.min(img_exp)) / (cp.max(img_exp) - cp.min(img_exp))
    img_out = cp.array(255*img_exp, dtype='uint8')

    img_YUV[:, :, 0] = img_out.get()

    return cv2.cvtColor(img_YUV, cv2.COLOR_YUV2BGR)