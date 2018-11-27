from compare import readData
import math
from createImage import readImage
if __name__ == '__main__':
    linelist,i=readData("./cmpResult")
    point1,point2,point3,point4,angle=linelist[0]
    print(linelist[0])
    x1,y1=point1
    x2,y2=point2
    x3,y3=point3
    x4,y4=point4
    x1=int(x1/4+3*x2/4)
    y1=int(3*y1/4+y2/4)
    x3 = int(x3/ 4 + 3 * x4 / 4)
    y3 = int(3 * y3 / 4 + y4 / 4)
    angle1=math.atan(abs((y1-y2)/(x1-x2)))
    angle2=math.atan(abs((y3-y4)/(x3-x4)))
    im1=readImage('./result/result1_line.jpg')
    im2=readImage('./result/result2_line.jpg')
    h1,w1=im1.shape[:2]
    h2,w2=im2.shape[:2]
    print("shape im1:",im1.shape[:2],"shape im2:",im2.shape[:2])
    print("angle1:",angle1,"angle2:",angle2)
    t_1=h1/h2 if h1/h2>1 else h2/h1
    t_2=w1/w2 if w1/w2>2 else w2/w1
    t=max(t_1,t_2)
    times=(t+1)/2+0.03
    length=200
    print("times:",times)
    if h1<h2:
        print("-"*10)
        x2,y2=x1+times*math.cos(angle1)*length,y1-times*math.sin(angle1)*length
        x4,y4=x3+math.cos(angle2)*length,y3-math.sin(angle2)*length
        with open("./modifyResult",'w') as f:
            f.write(str(((x1, y1), (int(x2), int(y2)), (x3, y3), (int(x4), int(y4)), abs(angle1 - angle2))))
    else:
        print(">"*10)
        x2,y2 = x1 +  math.cos(angle1) * length, y1 - length * math.sin(angle1)
        print(x2,y2)
        x4, y4 = x3 + times*math.cos(angle2) * length, y3 - times*math.sin(angle2) * length
        with open("./modifyResult",'w') as f:
            f.write(str(((x1,y1),(int(x2),int(y2)),(x3,y3),(int(x4),int(y4)),abs(angle1-angle2))))
            print("Done")