#-*-coding:utf-8-*-
#@author:lijinxi
import os
import math
import cv2
import numpy as np
from pylab import *
txtlist=[]
for txt in os.listdir('.'):
    if txt.endswith('.txt'):
        txtlist.append(txt)

def promot(file):
    lines=[]
    with open(file,'r') as f:
        for line in f:
            lines.append(list(eval(line)))
    print("lines:",lines,len(lines),sep='\n')
    newline=[]
    for line in lines:
        x1,y1,x2,y2=line
        if x1-x2==0:
            if math.sqrt((x1-x2)**2+(y1-y2)**2)>10:
                newline.append([x1,y1,x2,y2,90])
        elif 10<math.atan(abs((y2-y1)/(x2-x1)))*180/np.pi<80:
            continue
        elif math.sqrt((x1-x2)**2+(y1-y2)**2)>10:
            newline.append([x1,y1,x2,y2,math.atan((y2-y1)/(x2-x1))*180/np.pi])
    print("newline:",newline,len(newline),sep='\n')
    newlines2=retlines(newline,0)
    print('newlines2',newlines2,len(newlines2),sep='\n')
    return newlines2

def retlines(newline,index):
    length=len(newline)
    if length<=index:
        #print(newline)
        return newline
    newlines=[]
    for i in range(0,index):
        newlines.append(newline[i])
    x1, y1, x2, y2, _ = newline[index]
    newlines.append(newline[index])
    for i in range(index, length):
        x3, y3, x4, y4, _ = newline[i]
        if math.sqrt((x1 + x2 - x3 - x4) ** 2 / 4 + (y1 + y2 - y3 - y4) ** 2 / 4) < 20:
            continue
        else:
            newlines.append(newline[i])
    index+=1
    print(len(newlines),index)
    if length<=index:
        #print(newline)
        return newline
    return retlines(newlines,index)

lines=promot('1.txt')
print(lines)
with open("1_t.txt",'w') as f:
    for line in lines:
        f.write(str(line)+'\n')

im=np.zeros((2000,2000,3),dtype=np.uint8)+255

for line in lines:
    cv2.line(im,(line[0],line[1]),(line[2],line[3]),(0,0,255),2)
imshow(im)
imsave('1_t.png',im)
show()