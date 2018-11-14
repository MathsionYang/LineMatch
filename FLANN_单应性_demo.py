'''
单应性是一个条件,该条件表面当两幅图像中的一副出现投影畸变时还能
够彼此匹配
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT=10

img1=cv2.imread('images/8.png',0)
img2=cv2.imread('images/1.png',0)

sift=cv2.xfeatures2d.SIFT_create()
kp1,des1=sift.detectAndCompute(img1,None)
kp2,des2=sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE=0
index_params=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params=dict(checks=50)

flann=cv2.FlannBasedMatcher(index_params,search_params)
matches=flann.knnMatch(des1,des2,k=2)

good=[]
for m,n in matches:
    if m.distance<0.7*n.distance:
        good.append(m)

#在原始图像和训练图中发现关键点
if len(good)>MIN_MATCH_COUNT:
    src_pts=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    # 单应性
    #brief Finds a perspective transformation between two planes.
    M,mask=cv2.findHomography(src_pts,dst_pts,cv2.RANSAC,5.0)
    matchesMask=mask.ravel().tolist()
    #对第二张图像计算相对于原始目标的投影畸变,并绘制边框
    h,w=img1.shape
    pts=np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
    dst=cv2.perspectiveTransform(pts,M)

    img2=cv2.polylines(img2,[np.int32(dst)],True,255,3,cv2.LINE_AA)
else:
    matchesMask=None

draw_params=dict(matchColor=(0,255,0)
                     ,singlePointColor=None,
                     matchesMask=matchesMask,
                     flags=2)
img3=cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
plt.imshow(img3,'gray'),plt.show()