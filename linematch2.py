#-*-coding:utf-8-*-
#@author:lijinxi
from pylab import *
import numpy
import cv2

from compare import readData
lines,_=readData('./cmpResult2')
srcpoints=[]
dstpoints=[]
for line in lines:
    (x1,y1),(x2,y2),(x3,y3),(x4,y4),_,_=line
    srcpoints.append([x1,y1])
    srcpoints.append([x2,y2])
    dstpoints.append([x3,y3])
    dstpoints.append([x4,y4])
print(srcpoints)
print(dstpoints)
from createImage import readImage
im1=readImage("./result/1_processed_black_less.jpg")
im2=readImage('./result/7_processed_black_less.jpg')
H,mask=cv2.findHomography(np.array(srcpoints),np.array(dstpoints),
                       cv2.RANSAC, 5.0)

wrap = cv2.warpPerspective(im1, H, (im2.shape[1], im2.shape[0]))
#wrap[0:im2.shape[0], 0:im2.shape[1]] = im1
im3=cv2.addWeighted(wrap,0.5,im2,0.5,0)
imshow(im3)
show()
