import cv2
import random as rd

def getFil():
	fil = ['COLOR_BGR2YUV','COLOR_BGR2YUV', 'COLOR_BGR2YUV_I420','COLOR_BGR2LUV']
	return eval("cv2."+rd.choice(fil))

cap = cv2.VideoCapture(0)
f = [cv2.COLOR_BGR2HSV][0]
while True:
    success , img = cap.read()
    if cv2.waitKey(33) == ord("a"):
    	f = getFil()
    img = cv2.cvtColor(img,f)

    cv2.imshow("img",img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
    	break

