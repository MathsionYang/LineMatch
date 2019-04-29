#-*-coding:utf-8-*-
#@author:lijinxi
''' less black points ,erode or dilation '''
import cv2
from pylab import *
from PIL import Image


def readImage(filename):
    ''' read image '''
    im = array(Image.open(filename))
    if im is None:
        raise IOError("found no picture !")
    # imshow(im)
    # show()
    return im


def createImage(height=200, width=300):
    ''' create white image for special size '''
    im = np.zeros((height, width, 3), dtype=np.uint8)
    im = im+ 255
    # imshow(im)
    # x=ginput(1)
    # print(x)
    # show()
    return im

def oneColor(im,color):
    h,w=im.shape[:2]
    imgcopy=createImage(h,w)
    for i in range(0,h):
        for j in range(0,w):
            for k in range(0,3):
                if im[i,j][k]!=255:
                    imgcopy[i,j]=color
                    break
    '''
    imshow(imgcopy)
    show()
    '''
    return imgcopy

def lessBalckPoints(im, point, size_width=3, size_height=3, r=0.5):
    ''' less some areas which is full of points in black '''
    pointx, pointy = point
    count = 0
    for i in range(0, size_height):
        for j in range(0, size_width):
            if im[pointx + i, pointy + j].all() == 0:
                count = count + 1
    if count > size_width * size_height * r:
        im[pointx:pointx + size_height, pointy:pointy + size_width ]=[255,255,255]


def process(im, size=(3, 3), r=0.5):
    ''' divide areas and do lessBlackPoints '''
    # im=readImage(filename)
    height, width = im.shape[:2]  # height,width
    print(height,width,size)
    size_width, size_height = size
    h_t = height // size_width
    w_t = width // size_width
    print(h_t,w_t)
    for i in range(0, h_t):
        for j in range(0, w_t):
            lessBalckPoints(im, (i * size_height, j * size_width), size_width, size_height, r)
    # 处理边角

    for i in range(0, h_t):
        lessBalckPoints(im, (i * size_height, w_t * size_width), width - size_width * w_t, size_height, r)
    for j in range(0, w_t):
        lessBalckPoints(im, (size_height * h_t, j * size_width), size_width, height - h_t * size_height, r)
    lessBalckPoints(im, (size_height * h_t, size_width * w_t), width - size_width * w_t, height - h_t * size_height, r)

    #imshow(im)
    #show()
    return im


def im_erodeordilation(im, str,kernel,iteration):
    ''' erode or dilation '''
    k = np.ones(kernel, dtype=np.uint8)
    if str == 'erode':
        result = cv2.erode(im, k, iterations=iteration)
    elif str == 'dilation':
        result = cv2.dilate(im, k, iterations=iteration)
    elif str == "open":
        result = cv2.morphologyEx(im, cv2.MORPH_OPEN, k, iterations=iteration)
    elif str=="close":
        result = cv2.morphologyEx(im, cv2.MORPH_CLOSE, k, iterations=iteration)
    else:
        print("No matched !")
    imshow(result)
    show()
    return result



if __name__ == '__main__':
    '''
    im=readImage('./pictures/7_processed.png')
    black=oneColor(im,(0,0,0))
    imsave('./result/7_processed_black.jpg',black)


    im = readImage('./pictures/1_processed.png')
    black = oneColor(im, (0, 0, 0))
    imsave('./result/1_processed_black.jpg', black)
'''
    '''
    im=readImage("./result/1_processed_black.jpg")
    processed=process(im,size=(7,7),r=0.7)
    imsave("./result/1_processed_black_less.jpg",processed)
'''
    '''
    processed=readImage("./result/1_processed_black_less.jpg")
    str='open'
    im=im_erodeordilation(processed,str,(2,2),6)
    processed=process(im,(7,7),0.7)
    imsave("./result/1_processed_black_less_"+str+".png",im)
    '''

    im = readImage("./result/7_processed_black.jpg")
    processed = process(im, size=(7, 7), r=0.4)
    imsave("./result/7_processed_black_less.jpg", processed)

    '''
    processed = readImage("./result/7_processed_black_less.png")
    str = 'open'
    im = im_erodeordilation(processed, str, (2, 2), 6)
    processed = process(im, (5, 5), 0.8)
    imsave("./result/7_processed_black_less_" + str + ".png", im)
    '''