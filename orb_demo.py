'''
ORB与SIFT和SURF相比,具有更快的速度
基于FAST关键点检测的技术和基于BRIEF描述符的极速相结合
'''
'''
FAST算法会在像素周围绘制一个圆,该圆包括16个像素,
FAST会将每个像素与加上一个阈值的圆心像素进行比较,
若有连续、比加上一个阈值的圆心像素还亮或暗的像素,可认为圆心是角点
四分之三的测试像素必须在月至以内或意外,并将相应的像素标记为更亮或更暗
另外的四分之一的测试像素必须在该阈值的另一侧。
如果所有的像素都标记为更亮或更暗,或两个标记为更亮,而另外两个标记为更暗
则改像素就不是候选角点
'''
'''
BRIEF并不是特征检测,只是一个描述符。detectAndCompute函数检测的结果是一组
关键点,计算的结果是描述符。即opencv中的SIFT和SURF类即是检测器也是描述符
(实际上从算法本身来看,SIFT是DoG和SIFT的组合,SURF是快速Hession和SURF的组合)
关键点描述符是图像的一种表示,因此描述符可以作为特征匹配的一种方法
'''
'''
暴力匹配:描述符匹配方法,第一个描述符的所有特征与第二个描述符的特征进行比较，
每次比较给出一个距离值,最好的比较结果会被认为是一个匹配
使用BFMatcher对象来实现
'''
'''
ORB特征匹配包含了非常重要的一步:以旋转感知(rotation-aware)的方式使用
BRIEF,这样在训练图像与查询图像之间旋转差别很大的情况下也能提高匹配效果
'''
import numpy as np
import cv2
from matplotlib  import  pyplot as plt

'''
cv2.IMREAD_GRAYSCALE=0
cv2.IMREAD_ANYCOLOR=4
cv2.IMREAD_COLOR=1
cv2.IMREAD_LOAD_GDAL=8
cv2.IMREAD_UNCHANGED=-1
'''
img1=cv2.imread('result_line.jpg',cv2.IMREAD_GRAYSCALE)  #0
img2=cv2.imread('result2_line.jpg',cv2.IMREAD_GRAYSCALE)

orb=cv2.ORB_create()
# 创建ORB特征检测器和描述符
kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)
# 暴力匹配
'''
遍历描述符,确定描述符是否已经匹配,然后计算匹配质量(距离)排序
在一定置信度下显示前n个匹配,以此得到两幅图像是匹配的
'''
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)
img3=cv2.drawMatches(img1,kp1,img2,kp2,matches[:3],img2,flags=2)

'''
#KNN匹配,返回k个匹配
matches=bf.knnMatch(des1,des2,k=1)
img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,img2,flags=2)
'''
plt.imshow(img3),plt.show()