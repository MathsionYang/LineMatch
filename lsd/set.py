#-*-coding:utf-8-*-
#@author:lijinxi
import os
from lsd2 import lsd
import cv2
from pylab import *

dir=os.listdir('./pictures')

filelist=[]
for file in dir:
    if file.endswith('.jpg'):
        filelist.append(file)
print(filelist)


def getset(file,j):
    src = cv2.imread(file, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    lines = lsd(gray)
    with open(str(j) + '.txt', 'w') as f:
        for i in range(lines.shape[0]):
            pt1 = (int(lines[i, 0]), int(lines[i, 1]))
            pt2 = (int(lines[i, 2]), int(lines[i, 3]))
            width = lines[i, 4]
            #cv2.line(src, pt1, pt2, (0, 0, 255), 1)      #int(np.ceil(width / 2))
            f.write(str([pt1[0],pt1[1],pt2[0],pt2[1]]) + '\n')
        #imsave('./pictures/'+str(j)+'.png',src)
    print(lines)


i=0
for file in filelist:
    i=i+1
    getset('./pictures/'+file,i)