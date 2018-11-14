
import cv2
from matplotlib import pyplot as plt
from pylab import  *
from numpy import *

def choicePoints(file):
    img=cv2.imread(file)
    h,w=img.shape[:2]
    plt.imshow(img)
    points=ginput(3)
    print(points)
    plt.show()
    return h,w,points

#检测过的图

h1,w1,src=choicePoints('images/1.1.png')
h2,w2,dst=choicePoints('images/8.1.png')

# 原图
img1=array(cv2.imread('images/1.jpg',0))
img2=array(cv2.imread('images/8.jpg',0))

src1=[]
dst1=[]
for s in src:      # 元组转换列表,下一步float32
    src1.append(list(s))

for d in dst:
    dst1.append(list(d))
#以1.png的大小做变换,    需要将两张图片放到一个坐标系上,即先让一个点重合,
#然后选三对点,未先重合,这部分可以借助以前做的坐标系重合,且此步不需要缩放
M = cv2.getAffineTransform(np.float32(src1),np.float32(dst1))
res = cv2.warpAffine(img2,M,(w1,h1))
plt.imshow(res),plt.show()

# addWeight     大小需要一致,此步需要调试
cv2.addWeighted(img1, 0.5, res, 0.5, 0, img1)
plt.imshow(img1),plt.show()