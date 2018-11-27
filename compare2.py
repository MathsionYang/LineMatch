from compare import readData

lines1,_=readData('./image1_lines_output')
lines2,_=readData('./image2_lines_output')
#print(lines1)

def cmp2(linelist1,linelist2):
    cmplist=[]
    for line1 in linelist1:
        for line2 in linelist2:
            x1,y1=int(line1[0][0]/2+line1[1][0]/2),int(line1[0][1]+line1[1][1]/2)
            x2, y2 = int(line2[0][0] / 2 + line2[1][0] / 2), int(line2[0][1] + line2[1][1] / 2)
            cmplist.append((line1[0],line1[1],line2[0],line2[1],abs(line2[2]-line1[2]),abs((0.01*x1-0.01*x2)**2+(0.01*y1-0.01*y2)**2)))
    cmplist.sort(key=lambda l:l[5])
    cmplist.sort(key=lambda l:l[4])
    return cmplist
cmplist=cmp2(lines1,lines2)
print(cmplist)
with open("./cmpResult2",'w') as f:
    for l in cmplist[0:10]:
        f.write(str(l)+'\n')
