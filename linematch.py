from PIL import Image
from pylab import *
import math
import cv2
import random
from createImage import readImage,createImage
from compare import readData

def timesandangle(point1,point2,point3,point4):
    x1,y1=point1
    x2,y2=point2
    x3,y3=point3
    x4,y4=point4
    distance1=math.sqrt(((x1-x2)/100)**2+((y1-y2)/100)**2)
    print("distance1:",distance1)
    angle1=math.atan(abs((y1-y2)/(x1-x2)))
    distance2=math.sqrt(((x3-x4)/100)**2+((y3-y4)/100)**2)
    print("distance2:",distance2)
    angle2=math.atan(abs((y3-y4)/(x3-x4)))
    times=distance1/distance2
    angle=angle1-angle2
    print("times:",times,"angle:",angle)
    return times,angle

def widthandheight(im1,im2,times):
    h1,w1=im1.shape[:2]
    h2,w2=im2.shape[:2]
    if times<1:
        height=2*max(int(h1/times),h2)
        width=2*max(int(w1/times),w2)
        print(height,width)
        return height,width
    else:
        height =2* max(int(h2 *times), h1)
        width = 2*max(int(w2*times), w1)
        print(height,width)
        return height,width
def  rotate(im,basepoint,angle):
    RotateMatrix = cv2.getRotationMatrix2D((basepoint[0], basepoint[1]), angle=(180 * angle / np.pi), scale=1)
    RotImg = cv2.warpAffine(im, RotateMatrix, (im.shape[1] , im.shape[0]))
    return RotImg
def PictureNewFourPoints(im,basepoint,height,width):
    x1,y1=basepoint
    print(height,width)
    print("x1",x1,"y1:",y1)
    h,w=im.shape[0:2]
    print("hhhah",h,w)
    return ((width/2-x1,height/2-y1),(width/2+w-x1,height/2-y1),(width/2-x1,height/2+h-y1),(width/2+w-x1,height/2+h-y1))
def minPictureResize(im,times,basePoint):
    #times>1
    h,w=im.shape[:2]
    print("------",im.shape[:2])
    print("times:",times)
    im=cv2.resize(im,(int(w*times),int(h*times)),interpolation=cv2.INTER_CUBIC)
    print("--->",im.shape[:2])
    x1,y1=basePoint
    x1=x1*times
    y1=y1*times
    return (x1,y1,im)

if __name__ == '__main__':
    image1=readImage('./result_line.jpg')
    image2=readImage('./result2_line.jpg')
    #linelist,i=readData('./cmpResult')
    linelist, i = readData('./modifyResult')
    print(linelist)
    point1,point2,point3,point4,angle=linelist[0]
    print("-----")
    # 点可去1/4,3/4处
    times,angle=timesandangle(point1,point2,point3,point4)
    height,width=widthandheight(image1,image2,times)
    result_im1=createImage(height,width)
    result_im2=createImage(height,width)
    result_im=createImage(height,width)
    if times>1:
        fourpoints_1 = PictureNewFourPoints(image1, point1, height, width)
        x_1, x_2, x_3, x_4 = fourpoints_1
        print(fourpoints_1)
        x1, y1, im = minPictureResize(image2, times, point3)
        print('X1:', x1, "Y1:", y1, "shape:", im.shape[:2])
        fourpoints_2 = PictureNewFourPoints(im, (x1, y1), height, width)
        print(fourpoints_2)
        y_1, y_2, y_3, y_4 = fourpoints_2
        im2 = rotate(im, (x1, y1), angle)
        result_im1[int(x_1[1]):int(x_3[1]), int(x_1[0]):int(x_2[0])] = image1
        result_im2[int(y_1[1]):int(y_3[1]), int(y_1[0]):int(y_2[0])] = im2
        imshow(result_im1)
        imsave('./result_im1.jpg', result_im1)
        show()
        imshow(result_im2)
        imsave('./result_im2.jpg', result_im2)
        show()

        result_im = cv2.addWeighted(result_im1, 0.5, result_im2, 0.5, 0)
        imshow(result_im)
        imsave('result_im', result_im)
        show()
    else:
        print("PART B")
        fourpoints_1 = PictureNewFourPoints(image2, point3, height, width)
        x_1, x_2, x_3, x_4 = fourpoints_1
        print(fourpoints_1)
        x1, y1, im = minPictureResize(image1, 1/times, point1)
        print('X1:',x1,"Y1:",y1,"shape:",im.shape[:2])
        fourpoints_2 = PictureNewFourPoints(im, (x1, y1), height, width)
        print(fourpoints_2)
        y_1, y_2, y_3, y_4 = fourpoints_2
        im2 = rotate(im, (x1, y1), -angle)
        result_im1[int(x_1[1]):int(x_3[1]), int(x_1[0]):int(x_2[0])] = image2
        result_im2[int(y_1[1]):int(y_3[1]), int(y_1[0]):int(y_2[0])] = im2
        imshow(result_im1)
        imsave('./result_im1.jpg', result_im1)
        show()
        imshow(result_im2)
        imsave('./result_im2.jpg', result_im2)
        show()
        result_im = cv2.addWeighted(result_im1, 0.5,result_im2, 0.5, 0)
        imshow(result_im)
        imsave('result_im',result_im)
        show()


