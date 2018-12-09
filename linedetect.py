
import cv2
import numpy as np
import matplotlib.pyplot as plt

im1=plt.imread("./result/1_processed_black_less.jpg")
im1copy=im1.copy()
im2=plt.imread("./result/7_processed_black_less.jpg")
''''
gray1 = cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY)
gray1=cv2.GaussianBlur(gray1,(5,5),0)
edges = cv2.Canny(gray1, 50, 150, apertureSize=3)  # apertureSize参数默认其实就是3
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 60, minLineLength=400, maxLineGap=7)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(gray1, (x1, y1), (x2, y2), (0, 255,0))

'''
fig=plt.figure('MATCH')
#ax1=fig.add_subplot(121)
#ax1.imshow(im1,cmap='gray')
#ax2=fig.add_subplot(122)
#ax2.imshow(im2,cmap='gray')
plt.imshow(im1)
srcpoints=plt.ginput(7)
plt.show()

plt.imshow(im2)
dstpoints=plt.ginput(7)
plt.show()

print(im2.shape[:2])
print(srcpoints)
print(dstpoints)
H,mask=cv2.findHomography(np.array(srcpoints),np.array(dstpoints),
                       cv2.RANSAC, 5.0)

wrap = cv2.warpPerspective(im1, H, (im2.shape[1], im2.shape[0]))
#wrap[0:im2.shape[0], 0:im2.shape[1]] = im1
im3=cv2.addWeighted(wrap,0.5,im2,0.5,0)
plt.imshow(im3)
plt.show()


