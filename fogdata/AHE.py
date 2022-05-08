import cv2 as cv
import numpy as np


import numpy as np
import cv2 as cv
import time

# 彩色图像全局直方图均衡化
def hisEqulColor1(img):
    # 将RGB图像转换到YCrCb空间中
    ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
    # 将YCrCb图像通道分离
    channels = cv.split(ycrcb)
    # 对第1个通道即亮度通道进行全局直方图均衡化并保存
    cv.equalizeHist(channels[0], channels[0])
    # 将处理后的通道和没有处理的两个通道合并，命名为ycrcb
    cv.merge(channels, ycrcb)
    # 将YCrCb图像转换回RGB图像
    cv.cvtColor(ycrcb, cv.COLOR_YCR_CB2BGR, img)
    return img


# 彩色图像进行自适应直方图均衡化，代码同上的地方不再添加注释
def hisEqulColor2(img1):
    img = cv.imread(img1)
    time1 = time.time()

    ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
    channels = cv.split(ycrcb)

    # 以下代码详细注释见官网：
    # https://docs.opencv.org/4.1.0/d5/daf/tutorial_py_histogram_equalization.html
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe.apply(channels[0], channels[0])

    cv.merge(channels, ycrcb)
    cv.cvtColor(ycrcb, cv.COLOR_YCR_CB2BGR, img)

    time2 = time.time()



    img1 = "./AHE/data_beta_015.jpg"
    print(img1)
    cv.imwrite(img1, img)
    return time2-time1
hisEqulColor2('./FogImg/015.jpg')



