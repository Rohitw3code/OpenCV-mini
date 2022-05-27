import cv2
import random as rd
import numpy as np

cap = cv2.VideoCapture(0)

img1 = cv2.imread('oggy.webp')
img2 = cv2.imread('spider.jpg')

img1 = cv2.resize(img1,(450,450))
img2 = cv2.resize(img2,(450,450))

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

while True:
    s,f = cap.read()

    frame = cv2.resize(f,(450,450))
    res = cv2.addWeighted(frame,0.7,img1,0.3,0)

    cv2.imshow("f",res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()