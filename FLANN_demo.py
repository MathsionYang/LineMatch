'''
FLANN:最近邻的快速库
'''

import numpy as np
import cv2
from matplotlib import  pyplot as plt

queryImage=cv2.imread('result_line.jpg',0)
trainingImage=cv2.imread('result2_line.jpg',0)

sift=cv2.xfeatures2d.SIFT_create()
kp1,des1=sift.detectAndCompute(queryImage,None)
kp2,des2=sift.detectAndCompute(trainingImage,None)

#FLANN
'''
LinearIndex,KTreeIndex,KMeansIndex,CompositeIndex和AutotuneIndex
'''
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,tree=5)  #待处理核密度树的数量
searchParams=dict(checks=50)    #索引树要被遍历的层数

flann = cv2.FlannBasedMatcher(indexParams, searchParams)

matches = flann.knnMatch(des1, des2, k=2)
# 创建掩模
matchesMask = [[0, 0] for i in range(len(matches))]

for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        matchesMask[i] = [1, 0]

drawParams = dict(matchColor=(0, 255, 0),
                  singlePointColor=(255, 0, 0),
                  matchesMask=matchesMask,
                  flags=0
                  )
resultImage = cv2.drawMatchesKnn(queryImage, kp1, trainingImage, kp2, matches, None, **drawParams)
plt.xticks([]), plt.yticks([])
plt.imshow(resultImage), plt.show()



