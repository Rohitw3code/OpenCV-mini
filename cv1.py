import numpy as np
import cv2


# img = cv2.imread("rohit.jpg")

# lines = cv2.Canny(img,100,100)
# kernel = np.ones((5,5),np.uint8)
# dil = cv2.dilate(lines,kernel,iterations=1)
# cv2.imshow("image",dil)

# print(img.shape)

# im = cv2.resize(img,(300,200))
# im = img[0:500,0:500]

# cv2.imshow("img",im)
# cv2.imshow("img1",img)

img = np.zeros((512,512,3),np.uint8)
# img[50:100,0:100] = 25,10,60

cv2.line(img,(0,0),(512,512),(0,255,0),30)
cv2.rectangle(img,(10,10),(64,64),(0,0,255),3,cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"hello world",(100,350),cv2.FONT_HERSHEY_COMPLEX,1,(100,200,150),3)


cv2.imshow("i1",img)



cv2.waitKey()

# cap = cv2.VideoCapture(0)
# cap.set(10,100)


# while True:
# 	success , img = cap.read()
# 	# img1 = cv2.GaussianBlur(img,(7,7),10)
# 	# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 	kernal = np.ones((5,5),np.uint8)
# 	img = cv2.Canny(img,150,200)
# 	imgDialation = cv2.dilate(img,kernal,iterations=1)
# 	imgErode = cv2.erode(imgDialation,kernal,iterations=1)

# 	cv2.imshow("video1",imgErode)
# 	if cv2.waitKey(1) & 0xFF == ord("q"):
# 		break
