#-*-coding:utf-8-*-
#@author:lijinxi
def readData(filename):
    i=0
    linelist=[]
    with open(filename,"r") as f:
        for line in f:
            linelist.append(tuple(eval(line)))
            i+=1
    return linelist,i

def cmp(linelist1,linelist2):
    cmplist=[]
    for line1 in linelist1:
        for line2 in linelist2:
            cmplist.append((line1[0],line1[1],line2[0],line2[1],abs(line2[2]-line1[2])))
    cmplist.sort(key=lambda l:l[2])
    return cmplist[0]

if __name__ == '__main__':
    linelist1,_=readData('./image1_lines_output')
    linelist2,_=readData("./image2_lines_output")
    cmplist=cmp(linelist1,linelist2)
    with open("./cmpResult","w") as f:
        f.write(str(cmplist))