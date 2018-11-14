'''
尺度不变特征变换SIFT,通过一个特征向量来描述关键点周围区域的情况
'''

import cv2
import sys
import numpy as np
from matplotlib import  pyplot as plt
#imgpath=sys.argv[1]
#img=cv2.imread(imgpath)
img=cv2.imread('images/1.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #转为灰度图像

def fd(algorithm):
    if algorithm=='SIFT':
        return cv2.xfeatures2d.SIFT_create()  #创建sift对象
    if algorithm=='SURF':
        return cv2.xfeatures2d.SURF_create(10000)  #Hessian阈值为4000,阈值越高,能识别的特征就越少
fd_alg=fd('SURF')
#fd_alg=fd('SIFT')
keypoints,descriptor=fd_alg.detectAndCompute(gray,None)   #计算灰度图像,sift对象会使用DoG检测关键点
#并对每个关键点周围区域计算特征向量

img=cv2.drawKeypoints(image=img,outImage=img,keypoints=keypoints,
                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,   #绘制关键点
                      color=(51,163,236))
plt.imshow(img),plt.show()
'''
cv2.imshow('sift_keypoints',img)
while True:
    if cv2.waitKey(1000//12)&0xff==ord('q'):
        break
cv2.destroyAllWindows()
'''
'''
关键点有以下属性:
pt:表示图像中关键点的x坐标和y坐标
size:表示特征的直径
angle:表示特征的方向
response:表示关键点的强度
octave:表示特征所在金字塔的层级(算法在每次迭代(octave)时，作为参数的图像尺寸和相邻像素都会发生比变化
class_id:表示关键点的ID
'''