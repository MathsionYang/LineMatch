#-*-coding:utf-8-*-
#@author:lijinxi
from pylab import *
import numpy
import cv2
from LINE import line_detect_possible
from createImage import readImage
im1=readImage("demo1.png")
im2=readImage('demo2.png')
'''
image1,lines1=line_detect_possible(im1,100,5)
image2,lines2=line_detect_possible(im2,100,5)
for line in lines1:
    print(line[0])
for line in lines2:
    print(line[0])
'''
H,mask=cv2.findHomography(np.array([[113,232],[225,119],[291,135],[340,258]]),np.array([[79,271],[282,96],[343,125],[421,263]]),
                       cv2.RANSAC, 5.0)

wrap = cv2.warpPerspective(im1, H, (im1.shape[1], im1.shape[0]))
#wrap[0:im2.shape[0], 0:im2.shape[1]] = im1
im3=cv2.addWeighted(wrap,0.5,im2,0.5,0)
imshow(im3)
show()
