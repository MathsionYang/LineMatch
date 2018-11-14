import cv2
import numpy as np

img=cv2.imread('images/1.png')   #加载图片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #转为灰度格式
gray=np.float32(gray)
dst=cv2.cornerHarris(gray,2,23,0.04)
#cornerHarris第二个参数表示标记角点的记号的大小
#第三个参数限定了Sobel算子的中孔,角点检测的敏感度
img[dst>0.01*dst.max()]=[0,0,225]   #检测到的角点标记为红色
while True:
    cv2.imshow('corners',img)
    if cv2.waitKey(1000//12)&0xff==ord('q'):
        break
cv2.destoryAllWindows()

#cornerHarris跟图像的比例有关系,随图像比例的变化而检测到的角点随之变化