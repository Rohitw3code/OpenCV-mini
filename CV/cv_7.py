import cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rd

img = cv2.imread('spider.jpg')

def createFilter():
	lst =[]
	for i in range(8):
		l = []
		for j in range(5):
			l.append(rd.randint(0,2)/rd.randint(10,50))
		lst.append(l)
	return np.float32(lst)


# kernel = np.ones((3,3),np.float32)/9
# dst = cv2.filter2D(img,-1,kernel)

img1 = cv2.blur(img,(5,5))
img2 = cv2.GaussianBlur(img,(5,5),0)
img3 = cv2.medianBlur(img,5)
img4 = cv2.bilateralFilter(img,9,75,75)

# cv2.imshow('Original',img)
# cv2.imshow('Blur',img1)
# cv2.imshow('GaussianBlur',img2)
# cv2.imshow('medianBlur',img3)
cv2.imshow('biLateral',img4)

cap = cv2.VideoCapture(0)
while True:
	s,frame = cap.read()
	frame = cv2.flip(frame,1)
	mb = cv2.medianBlur(frame,5)
	bl = cv2.bilateralFilter(frame,9,75,75)
	canny = cv2.Canny(bl,100,200)


	cv2.imshow("original",frame)
	cv2.imshow("frame",canny)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break






cv2.waitKey(0)
cv2.destroyAllWindows()