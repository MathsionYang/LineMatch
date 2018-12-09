from compare import readData
import numpy as np
import cv2
from pylab import *
lines1,_=readData('./image1_lines_output')
lines2,_=readData('./image2_lines_output')
#print(lines1)
def meth(linelist):
    linelist1=[]
    set={}
    num=len(linelist)
    for i in range(0,num):
        line=linelist[i]
        (x1,y1),(x2,y2)=line[0],line[1]
        for j in range(i+1,num):
            (x3,y3),(x4,y4)=[]
    pass
def cmp2(linelist1,linelist2):
    cmplist=[]
    for line1 in linelist1:
        for line2 in linelist2:
            x1,y1=int(line1[0][0]/2+line1[1][0]/2),int(line1[0][1]+line1[1][1]/2)
            x2, y2 = int(line2[0][0] / 2 + line2[1][0] / 2), int(line2[0][1] + line2[1][1] / 2)
            cmplist.append((line1[0],line1[1],line2[0],line2[1],abs(line2[2]-line1[2]),abs((0.01*x1-0.01*x2)**2+(0.01*y1-0.01*y2)**2)))
    cmplist.sort(key=lambda l:sqrt(l[4]**2+l[5]**2))
    return cmplist
cmplist=cmp2(lines1,lines2)
print(cmplist)
with open("./cmpResult2",'w') as f:
    for l in cmplist[0:10]:
        f.write(str(l)+'\n')

'''
im=np.zeros((2000,2000,3),dtype=np.uint8)+255
for line in lines1:
    cv2.line(im,line[0],line[1],(0,255,255),2)
for line in lines2:
    cv2.line(im,line[0],line[1],(255,0,0),2)

imshow(im)
show()
'''