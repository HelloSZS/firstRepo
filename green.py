import random
import cv2
import numpy as np
import math
from PIL import Image


img_path = 'C:\\Users\\Nelson\\Desktop\\cut\\2\\18.jpg'

img = cv2.imread(img_path,cv2.IMREAD_COLOR)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# (400,400,3)
# (B,G,R)
#
# random_flip(img)
# print(img.shape)
# random_flip(img,[200,200,300,300],)
print(img.shape)


rows = img.shape[0]
cols = img.shape[1]
#或者可以这样写
rows, cols = img.shape[:2]

#https://blog.csdn.net/m0_38007695/article/details/82718107
#灰度直方图，图像增强
def grayH(img):
    #1.要把图片的h和w找出来
    #2.第二步，统计每个亮度的像素点个数
    h, w = img.shape[:2]

    #0~255
    grayHist = np.zeros([256],np.uint64)
    print(grayHist)
    for i in range(h):
        for j in range(w):
            grayHist[img[i][j]] += 1
            # grayHist [0 * 256]

    print(grayHist)
    return grayHist

grayH(img)
a = np.linspace(0,255,256)
print(a)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(a,grayH(img),c="black")
plt.ylabel(u"该灰度值个数")
plt.xlabel(u"灰度值")
plt.show()


# # cols-1 和 rows-1 是坐标限制
#
# #M 图片中心点
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),30,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
pts1 = np.float32([[230,230],[368,52],[28,387],[399,399]])
pts2 = np.float32([[0,0],[399,0],[0,399],[399,399]])


#5透视变换
M = cv2.getPerspectiveTransform(pts1,pts2)
dst2 = cv2.warpPerspective(img,M,(300,300))

# plt.figure()
# plt.subplot(121)
# plt.plot(img.shape[:2],img)
# plt.subplot(122)
# plt.plot(dst2.shape[0],dst2.shape[1],dst2)

#python 读取并显示图片的两种方法
#https://www.cnblogs.com/yinxiangnan-charles/p/5928689.html
img2 = img[:,:,0]

#热量图
plt.figure()
plt.subplot(121)
plt.imshow(img2)

#灰度图
plt.subplot(122)
plt.imshow(img2,cmap='Greys_r')
plt.show()


# cv2.imshow('image2',dst2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# #
# # import time
# # time.sleep(1000)
#
# # scaler = np.stack([400, 300], axis=0)
# # print(scaler)
# # #这里用(1,2)或者[1,2]都可以
# # center = np.reshape(0.5 * scaler, (1,2))
# # print(center.shape)