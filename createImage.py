import cv2
import os
from pylab import *
from PIL import Image

def readImage(filename):
    im=array(Image.open(filename))
    if im is None:
        raise IOError("found no picture !")
    #imshow(im)
    #show()
    return im

def createImage(height=200,width=300):
    im=np.zeros((height,width,3),dtype=np.uint8)
    im=im+255
    #imshow(im)
    #x=ginput(1)
    #print(x)
    #show()
    return im

def point_charge(im,point,size_width=3,size_height=3,r=0.5):
    pointx,pointy=point
    count=0
    for i in range(0,size_height):
        for j in range(0,size_width):
            if im[pointx+i,pointy+j].all()==0:
                count=count+1
    if count>size_width*size_height*r:
        im[pointx:pointx+size_height-1,pointy:pointy+size_width-1]=[255,255,255]

def process(im,size=(3,3),r=0.5):
    #im=readImage(filename)
    height,width=im.shape[:2]  #height,width
    size_width,size_height=size
    h_t=height//size_width
    w_t=width//size_width
    for i in range(0,h_t):
        for j in range(0,w_t):
            point_charge(im,(i*size_height,j*size_width),size_width,size_height,r)
    # 处理边角
    for i in range(0,h_t):
        point_charge(im,(i*size_height,w_t*size_width),width-size_width*w_t,size_height,r)
    for j in range(0,w_t):
        point_charge(im,(size_height*h_t,j*size_width),size_width,height-h_t*size_height,r)
    point_charge(im,(size_height*h_t,size_width*w_t),width-size_width*w_t,height-h_t*size_height,r)
    imshow(im)
    show()
    return im
def im_erodeordilation(im,str):
    k = np.ones((2, 2), dtype=np.uint8)
    if str=='erode':
        result=cv2.erode(im,k,iterations=10)
    elif str=='dilation':
        result = cv2.dilate(im, k, iterations=10)
    elif str=="open":
        result=cv2.morphologyEx(im, cv2.MORPH_OPEN, k,iterations=20)
    else :
        result=cv2.morphologyEx(im, cv2.MORPH_CLOSE, k,iterations=10)
    imshow(result)
    show()
    return result
def line_detect_possible(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)  # apertureSize参数默认其实就是3
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 60, minLineLength=250, maxLineGap=15)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    imshow(image)
    show()
    return image,lines

if __name__ == '__main__':
    '''
    im=readImage("./pictures/1_processed.png")
    im=im_erodeordilation(im,'erode')
    im=im_erodeordilation(im,"dilation")
    #createImage(height,width)
    im=process(im,(9,9),r=0.25)
    imsave("result.jpg",im)
    '''
    '''
    im=readImage('./result.jpg')
    line_detect_possible(im)
    '''
    '''
    im = readImage("./pictures/7_processed.png")
    im = im_erodeordilation(im, 'erode')
    im = im_erodeordilation(im, "dilation")
    # createImage(height,width)
    im = process(im, (5, 5), r=0.1)
    imsave("result2.jpg", im)
'''
    im = readImage('./result.jpg')
    im,_=line_detect_possible(im)
    imsave("result_line.jpg",im)