#-*-coding:utf-8-*-
#@author:lijinxi
from lsd2 import lsd
import cv2
import numpy as np
import os
fullName = '../pictures/2.jpg'
src = cv2.imread(fullName, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
lines = lsd(gray)
for i in range(lines.shape[0]):
    pt1 = (int(lines[i, 0]), int(lines[i, 1]))
    pt2 = (int(lines[i, 2]), int(lines[i, 3]))
    width = lines[i, 4]
    cv2.line(src, pt1, pt2, (0, 0, 255), 1)      #int(np.ceil(width / 2))
cv2.imshow('',src)
cv2.waitKey()