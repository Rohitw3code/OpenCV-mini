import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while True:
    success , img = cap.read()
    img = cv2.flip(img,1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(img,kernel,iterations = 1)
    dilation = cv2.dilate(img,kernel,iterations = 1)

    cv2.imshow("img",img)
    cv2.imshow("eros",erosion)
    cv2.imshow("dila",dilation)
    if cv2.waitKey(1) & 0xFF == ord("q"):
    	break

