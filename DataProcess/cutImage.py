import cv2
import os
import pandas as pd
import numpy as np
def cutimage(dir, loction):
    for root, dirs, files in os.walk(dir):
        for file in files:
            filepath = "../Img/" + file
            image = cv2.imread(filepath)  # opencv剪切图片
            print(file)
            #x1, y1, x2, y2 = getLoc(file, loc)
            #image = image[y1:y2, x1:x2, ]
            #print(x1, y1, x2, y2)
            dim = (300, 200)  # 指定尺寸w*h
            resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  # 这里采用的插值法是INTER_LINEAR
            #gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            #cv2.imwrite("../cut/%s" % file, image)
            cv2.imwrite("../rgb/%s" % file, resized)  # 保存文件
            #cv2.imwrite("../gary/%s" % file, gray)  # 保存文件
    cv2.waitKey(0)  # 退出

def getLoc(filename, loction):
    for i in range(8144):
        if(loction[i,1] == filename):
            return loction[i,2],loction[i,3],loction[i,4],loction[i,5]
    print(filename+"error1")
    return 0, 0, 0, 0


dir = '../Img'
loc = pd.read_csv("../data/data.csv")
loc = np.array(loc)
cutimage(dir, loc)
