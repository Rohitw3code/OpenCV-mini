import numpy as np
import cv2
im = cv2.imread('spider.jpg',1)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# for data in contours:
# 	print("The contours have this data %r" %data)


mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,contours[0],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
mean_val = cv2.mean(im,mask = mask)

cnt = max(contours, key = cv2.contourArea)
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

cv2.drawContours(im,cnt,-1,(0,255,0),3)

cv2.circle(im,leftmost, radius=10, color=(0, 0, 255), thickness=-1)
cv2.circle(im,rightmost, radius=10, color=(0, 0, 255), thickness=-1)
cv2.circle(im,topmost, radius=10, color=(0, 0, 255), thickness=-1)
cv2.circle(im,bottommost, radius=10, color=(0, 0, 255), thickness=-1)

print(leftmost)



cv2.imshow('output',im)
while True:
    if cv2.waitKey(6) & 0xff == 27:
    	break