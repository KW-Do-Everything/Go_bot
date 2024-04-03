import cv2
import numpy as np


def CLAHE(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    if len(img.shape) == 3:
        y, u, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2YUV))
        Y = clahe.apply(y)
        return cv2.cvtColor(cv2.merge((Y, u, v)), cv2.COLOR_YUV2BGR)
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


def homomorphic_filter(img):
    img_YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y = img_YUV[:, :, 0]

    rows = y.shape[0]
    cols = y.shape[1]

    # illumination elements와 reflectance elements를 분리하기 위해 log 취하기
    imgLog = np.log1p(np.array(y, dtype='float') / 255) # y를 0-1 사이로 만든뒤 log

    # frequency를 이미지로 나타내면 4분면에 대칭으로 나타남
    # 4분면중 하나에 이미지를 대응시키기위해 row, col을 두배
    M = 2 * rows + 1
    N = 2 * cols + 1

    # 가우시안 마스크 생성 sigma=10
    sigma=10
    (X, Y) = np.meshgrid(np.linspace(0, N-1, N), np.linspace(0, M-1, M))
    Xc = np.ceil(N/2)
    Yc = np.ceil(M/2)

    gaussianNumerator = (X - Xc)**2 + (Y - Yc)**2

    # LPF와 HPF
    LPF = np.exp(-gaussianNumerator / (2*sigma*sigma))
    HPF = 1 - LPF

    LPF_shift = np.fft.ifftshift(LPF.copy())
    HPF_shift = np.fft.ifftshift(HPF.copy())

    img_FFT = np.fft.fft2(imgLog.copy(), (M, N))
    img_LF = np.real(np.fft.ifft2(img_FFT.copy() * LPF_shift, (M, N)))
    img_HF = np.real(np.fft.ifft2(img_FFT.copy() * HPF_shift, (M, N)))

    gamma1 = 0.3
    gamma2 = 1.5
    img_adjusting = gamma1 * img_LF[0:rows, 0:cols] + gamma2 * img_HF[0:rows, 0:cols]

    img_exp = np.expm1(img_adjusting)
    img_exp = (img_exp - np.min(img_exp)) / (np.max(img_exp) - np.min(img_exp))
    img_out = np.array(255*img_exp, dtype='uint8')

    img_YUV[:, :, 0] = img_out

    return cv2.cvtColor(img_YUV, cv2.COLOR_YUV2BGR)