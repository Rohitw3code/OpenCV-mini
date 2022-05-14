import cv2
import numpy as np

img = cv2.imread("cards.jpg")
img = cv2.resize(img,(512,512))

width = 250
height = 350

pts1 = np.float32([[342,81],[550,106],[294,309],[515,342]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

img = cv2.warpPerspective(img,matrix,(250,350))


cv2.imshow("image",img)


cv2.waitKey(0)