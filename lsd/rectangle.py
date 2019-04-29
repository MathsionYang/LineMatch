#-*-coding:utf-8-*-
#@author:lijinxi
import math
lines=[]
with open('conpoints.txt','r')  as f:
    for line in f:
        lines.append(list(eval(line)))
print(lines)
len1=len(lines)
for i in range(0, len1):
    x1, x2, y1, y2, a1 = lines[i]
    h_lines=[]
    v_i=0
    h_i=0
    for j in range(i+1,len1):
        if abs(a1)>60:
            v_i+=1
            x3,y3,x4,y4,a2=lines[j]
            if abs(abs(a1)-abs(a2))<20:
                if max(y1,y2)<min(y3,y4) and abs( (x1+x2-x3-x4)/2)<6:
                    x1,x2,y1,y2,a1=lines[j]
                    v_i+=1
            if abs(abs(a1)-abs(a2))>60:
                if max(x1,x2)<min(x3,x4) and min(x3,x4)-max(x1,x2)<6 and abs(min(y3,y4)-min(y1,y2))<6:
                    h_i+=1
                    x1, x2, y1, y2, a1 = lines[j]







