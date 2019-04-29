#-*-coding:utf-8-*-
#@author:lijinxi
import os
import cv2
from PIL import  Image
from pylab import *
def line(graphfile,im,num):
    graph={}
    with open(graphfile) as f:
        graph=dict(eval(f.read()))
    print(graph)
    keylist=[]
    for key,value in graph.items():
        keylist.append(key)
    for key in keylist:
        one=list(eval(key))

        if num==2:   #graph
            two, three = graph[key]
            if abs(one[4])>50:
                cv2.line(im,(one[0],one[1]),(one[2],one[3]),(255,0,0),3)
                #cv2.line(im,(two[0],two[1]),(two[2],two[3]),(0,255,0),3)
                #cv2.line(im, (three[0], three[1]), (three[2], three[3]), (255, 0, 0), 3)
            else:
                cv2.line(im, (one[0], one[1]), (one[2], one[3]), (255, 0, 0), 3)
                #cv2.line(im, (two[0], two[1]), (two[2], two[3]), (0, 255, 0), 3)
                #cv2.line(im, (three[0], three[1]), (three[2], three[3]), (255, 0, 0), 3)
        if num==0:  #hegraph
            two= graph[key]
            if abs(one[4])>50:
                cv2.line(im,(one[0],one[1]),(one[2],one[3]),(0,255,0),3)
                #cv2.line(im,(two[0],two[1]),(two[2],two[3]),(255,0,0),3)
            else:
                cv2.line(im, (one[0], one[1]), (one[2], one[3]), (0, 255, 0), 3)
                #cv2.line(im, (two[0], two[1]), (two[2], two[3]), (255, 0, 0), 3)
        if num==1:  #vgraph
            two= graph[key]
            if abs(one[4])>50:
                cv2.line(im,(one[0],one[1]),(one[2],one[3]),(0,0,255),3)
                #cv2.line(im,(two[0],two[1]),(two[2],two[3]),(0,255,0),3)
            else:
                cv2.line(im, (one[0], one[1]), (one[2], one[3]), (0, 0, 255), 3)
                #cv2.line(im, (two[0], two[1]), (two[2], two[3]), (0, 255, 0), 3)
    return im
if __name__ == '__main__':
        im = array(Image.open("./pictures/1_processed_black_less.png"))
        h, w = im.shape[:2]
        im = np.zeros((h, w, 3), dtype=np.uint8) + 255
        im=line('hgraph.txt',im,0)
        im=line('graph.txt',im,2)
        im=line('vgraph.txt',im,1)
        imshow(im)
        show()