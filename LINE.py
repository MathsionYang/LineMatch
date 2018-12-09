#直线检测
#使用霍夫直线变换做直线检测，前提条件：边缘检测已经完成
import cv2 as cv
import os
import numpy as np
from pylab import  *
from PIL import  Image
from createImage import readImage,createImage
import math

#统计概率霍夫线变换
def line_detect_possible(image,minLength=60,maxGap=5):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # apertureSize参数默认其实就是3
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 60, minLineLength=minLength, maxLineGap=maxGap)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (172, 255,0), 1)
    return image,lines
def oncallback1(x):
    image1 = readImage('./result/1_processed_black_less.jpg')
    filename = "image1_lines_output"
    minLineLength=cv.getTrackbarPos('minLineLength','image1_HoughLine and save')
    maxLineGap=cv.getTrackbarPos("maxLineGap",'image1_HoughLine and save')
    save=cv.getTrackbarPos('save:1 no:0',"image1_HoughLine and save")
    image,lines=line_detect_possible(image1,minLineLength,maxLineGap )
    if save==1:
        linesave(lines,filename)
        imsave("./result/result1_line.jpg",image)
    imshow(image)
    show()

def oncallback2(x):
    image2 = readImage('./result/7_processed_black_less.jpg')
    filename="image2_lines_output"
    minLineLength=cv.getTrackbarPos('minLineLength','image2_HoughLine and save')
    maxLineGap=cv.getTrackbarPos("maxLineGap",'image2_HoughLine and save')
    save=cv.getTrackbarPos('save:1 no:0',"image2_HoughLine and save")
    image,lines=line_detect_possible(image2,minLineLength,maxLineGap )
    if save==1:
        linesave(lines,filename)
        imsave("./result/result2_line.jpg",image)
    imshow(image)
    show()
def linesave(lines,filename):
    lists=[]
    i=0
    with open(filename,"w") as f:
        for line in lines:
            i=i+1
            x1, y1, x2, y2 = line[0]
            if x1==x2 or y1==y2:
                continue
            angle=math.atan(abs((y1-y2)/(x1-x2)))/math.pi*180
            if  angle>80 or angle<10:
                continue
            lists.append(((x1,y1),(x2,y2),angle,i))
        lists.sort(key=lambda l:-l[2])
        for list1 in lists:
            f.write(str(list1)+'\n')
def Trackbar():
    im=np.zeros((100,1900),dtype=np.uint8)
    im=im+255
    cv.namedWindow("image1_HoughLine and save",cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("minLineLength",'image1_HoughLine and save',50,400,oncallback1)
    cv.createTrackbar("maxLineGap","image1_HoughLine and save",0,50,oncallback1)
    cv.createTrackbar('save:1 no:0','image1_HoughLine and save',0,1,oncallback1)
    cv.namedWindow("image2_HoughLine and save", cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("minLineLength", 'image2_HoughLine and save', 50, 400, oncallback2)
    cv.createTrackbar("maxLineGap", "image2_HoughLine and save", 0, 50, oncallback2)
    cv.createTrackbar('save:1 no:0', 'image2_HoughLine and save', 0, 1, oncallback2)
    cv.imshow("image1_HoughLine and save",im)
    cv.imshow("image2_HoughLine and save",im)
    cv.waitKey()
if __name__ == '__main__':
    Trackbar()