#-*-coding:utf-8-*-
#@author:lijinxi
from pylab import *
import cv2
from PIL import Image
import math
def rect(imfile,linefile):
    lines=[]
    with open(linefile,'r') as f:
        for line in f:
            lines.append(list(eval(line)))
    print(lines)
    im=array(Image.open(imfile))
    h,w=im.shape[:2]
    print(h,w)
    graph={}
    hgraph={}
    vgraph={}
    len1=len(lines)
    for i in range(0,len1):
        x1, y1, x2, y2, a1 = lines[i]
        h_line = []
        v_line = []
        for j in range(i+1,len1):
            x3, y3, x4, y4, a2 = lines[j]
            #minnum = min([math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2), math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2),
                          #math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2), math.sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)])
            if abs(a1)<10:
                if abs(abs(a1)-abs(a2))<20:
                    minnum=0
                    if max(x1,x2)<min(x3,x4):

                        if min(y1,y2)>max(y3,y4):
                            minnum=math.sqrt((max(x1,x2)-min(x3,x4))**2+(min(y1,y2)-max(y3,y4))**2)
                        elif max(y1,y2)<min(y3,y4):
                            minnum = math.sqrt((max(x1, x2) - min(x3, x4)) ** 2 + (max(y1 , y2) - min(y3,y4)) ** 2)
                        #minnum=math.sqrt((max(x1,x2)-min(x3,x4))**2+((y1+y2)/2-(y3+y4))**2)
                        if 0<minnum<45:
                            #h_line.append([x3,y3,x4,y4,abs(a1-a2),minnum,abs((y1+y2-y3-y4)/2)])
                            h_line.append(str([x3, y3, x4, y4, abs(a1 - a2), minnum, abs((y1 + y2 - y3 - y4) / 2)]))
                elif abs(abs(a1)-abs(a2))>40:
                    minnum=0
                    if max(y1,y2)<min(y3,y4):

                        if min(x1,x2)>max(x3,x4):
                            minnum=math.sqrt((max(y1,y2)-min(y3,y4))**2+(min(x1,x2)-max(x3,x4))**2)
                        elif min(x1,x2)<min(x3,x4):
                            minnum = math.sqrt((max(y1, y2) - min(y3, y4)) ** 2 + (min(x1, x2) - min(x3, x4)) ** 2)

                        #minnum = math.sqrt((max(y1, y2) - min(y3, y4)) ** 2)
                    if 0<minnum<45:
                        #v_line.append([x3,y3,x4,y4,abs(a1-a2),minnum,abs((min(x1,x2)-(x3+x4)/2))])
                        v_line.append(str([x3, y3, x4, y4, abs(a1 - a2), minnum, abs((min(x1, x2) - (x3 + x4) / 2))]))
            if abs(a1)>10:
                if abs(abs(a1) - abs(a2)) > 40:
                    minnum = 0
                    if max(x1, x2) < min(x3, x4):

                        if min(y1, y2) > max(y3, y4):
                            minnum = math.sqrt((max(x1, x2) - min(x3, x4)) ** 2 + (min(y1, y2) - max(y3, y4)) ** 2)
                        elif min(y1, y2) > min(y3, y4):
                            minnum = math.sqrt((max(x1, x2) - min(x3, x4)) ** 2 + (max(y1, y2) - min(y3 ,y4)) ** 2)

                        #minnum = math.sqrt((max(x1, x2) - min(x3, x4)) ** 2 )
                        if 0 < minnum < 45:
                            #h_line.append([x3, y3, x4, y4, abs(a1 - a2), minnum,abs((min(x3,x4)-(x1+x2)/2))])
                            h_line.append(str([x3, y3, x4, y4, abs(a1 - a2), minnum, abs((min(x3, x4) - (x1 + x2) / 2))]))
                elif abs(abs(a1) - abs(a2)) <20:
                    minnum = 0
                    if max(y1, y2) < min(y3, y4):

                        if min(x1, x2) > max(x3, x4):
                            minnum = math.sqrt((max(y1, y2) - min(y3, y4)) ** 2 + (min(x1, x2) - max(x3, x4)) ** 2)
                        elif min(x1, x2) < min(x3, x4):
                            minnum = math.sqrt((max(y1, y2) - min(y3, y4)) ** 2 + (min(x1, x2) - min(x3, x4)) ** 2)

                        #minnum = math.sqrt((max(y1, y2 )- min(y3, y4)) ** 2 + ((x1 + x2) / 2 - (x3 + x4)) ** 2)
                    if 0 < minnum < 45:
                        #v_line.append([x3, y3, x4, y4, abs(a1 - a2), minnum,abs((x1+x2-x3-x4)/2)])
                        v_line.append(str([x3, y3, x4, y4, abs(a1 - a2), minnum, abs((x1 + x2 - x3 - x4) / 2)]))
        if abs(a1)<10:
            h_line.sort(key=lambda l:list(eval(l))[6])
            v_line.sort(key=lambda l:list(eval(l))[6])
        if abs(a1)>10:
            h_line.sort(key=lambda l:list(eval(l))[6])
            v_line.sort(key=lambda l:list(eval(l))[6])
        #print('vline',h_line,'hline',v_line,sep='\n')

        if len(h_line) ==0 and len(v_line)==0:
            continue
        elif  len(v_line)==0:
           hgraph.update({str(lines[i]): [h_line[0],0]})                    #hgraph
        elif len(h_line)==0:
            vgraph.update({str(lines[i]):[ v_line[0],1]})
        else:
            graph.update({str(lines[i]):[h_line[0],v_line[0]]})
    #print(graph,len(graph))
    #print(vgraph)
    #print(hgraph)
    with open('graph.txt','w') as f:
        f.write(str(graph))
        f.flush()
    with open('vgraph.txt',"w" ) as f:
        f.write(str(vgraph))
        f.flush()
    with open('hgraph.txt','w') as f:
        f.write(str(hgraph))
        f.flush()
    return graph,vgraph,hgraph
def maxin(graph,vgraph,hgraph):
    graph.update(vgraph)
    graph.update(hgraph)
    len1=len(graph)
    print("graph:",graph)
    keylist=[]
    result=[]
    for key,value in graph.items():
        keylist.append(key)
    for i in range(0,len1):
        flag=1
        h_i = 0
        v_i = 0
        if graph[keylist[i]] is not None:
            h_i += 1
            v_i += 1
            hkey =graph.get(keylist[i])[0]
            vkey = graph.get(keylist[i])[1]
            print('第i:' + str(i) + '次:')
            print(hkey, vkey)
        while flag:

            if graph.get(hkey) :
                if isinstance(graph.get(hkey)[1],str):

                    h_i += 1
                    hkey = graph.get(hkey)[0]
                    print('done1')
                    print("hkey:",hkey)
                elif graph.get(hkey)[1]==0:
                    h_i += 1
                    hkey = graph.get(hkey)[0]
                    print('done2')
                    print("hkey:", hkey)
                elif graph.get(hkey)[1]==1:
                    print('done3h')
                    continue
            if graph.get(vkey) :
                if isinstance(graph.get(hkey)[1], str):
                    v_i += 1
                    vkey = graph.get(vkey)[1]
                    print('done1')
                    print("vkey:", vkey)
                elif graph.get(hkey)[1]==1:
                    v_i += 1
                    vkey = graph.get(vkey)[0]
                    print('done2')
                    print("vkey:", vkey)
                elif  graph.get(hkey)[1]==0:
                    print('done3v')
                    continue
            if  graph.get(hkey) is None and  graph.get(vkey) is None:
                flag=0
        result.append([list(eval(keylist[i])),h_i*v_i])
    result.sort(key=lambda l:-l[1])
    #for r in result:
        #print(r)

if __name__ == '__main__':
    graph,vgraph,hgraph=rect('./pictures/1.png','1_t.txt')
    maxin(graph,vgraph,hgraph)
    #rect('./pictures/2.png', '2_t.txt')
    #rect('./pictures/1.png', '1_t.txt')