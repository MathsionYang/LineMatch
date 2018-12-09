from pylab import *
import cv2
def conpoint(graphfile1,graphfile2,graphfile3):
    graph={}
    conpoints=[]
    with open(graphfile1,'r') as f:
        graph=dict(eval(f.read()))
    for key,val in graph.items():
        conpoints.append(list(eval(key)))
    print(len(conpoints))
    with open(graphfile2,'r') as f:
        graph=dict(eval(f.read()))
    for key,val in graph.items():
        conpoints.append(list(eval(key)))
    print(len(conpoints))
    with open(graphfile3,'r') as f:
        graph=dict(eval(f.read()))
    for key,val in graph.items():
        conpoints.append(list(eval(key)))
    print(len(conpoints))
    print(conpoints)
    return  conpoints
if __name__ == '__main__':
    conpoints=conpoint('graph.txt','vgraph.txt','hgraph.txt')
    im=np.zeros((1500,1800,3),dtype=np.uint8)+255
    for p in conpoints:
        cv2.line(im,(p[0],p[1]),(p[2],p[3]),(0,255,0),3)
    imshow(im)
    show()
    with open('conpoints.txt','w') as f:
        for p in conpoints:
            f.write(str(p)+'\n')