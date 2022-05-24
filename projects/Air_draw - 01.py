import cv2
import numpy as np
import random as rd

cap = cv2.VideoCapture(0)

drawPoints = []
font = cv2.FONT_HERSHEY_SIMPLEX


def getContours(img):
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x,y,w,h = 0,0,0,0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(canvas, cnt, -1, (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)), 3)
            epsilon = 0.1*cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,epsilon,True)            
            x, y, w, h = cv2.boundingRect(approx)

            center = (x+w//2, y+h//2)
            cv2.circle(applyImg,center,20,(0,0,255),-1)
            cv2.putText(applyImg,"Red",(x,y),font,4,(0,0,0),2,cv2.LINE_AA)
            cv2.rectangle(applyImg,(x,y),(x+w,y+h),(0,255,0),3)
    return x+w//2,y

while True:
    success, img = cap.read()
    frame = cv2.flip(img, 1)
    imgRes = frame.copy()
    # create canvas
    canvas = np.ones((550,550,3),np.uint8)*255
    applyImg = canvas

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ret1, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # # Otsu's thresholding
    # ret2, th2 = cv2.threshold(
    #     gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # # Otsu's thresholding after Gaussian filtering
    # blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # ret3, th3 = cv2.threshold(
    #     blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    imgHsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_hsv = np.array([64,117,177])
    upper_hsv = np.array([174,185,255])

    mask = cv2.inRange(imgHsv,lower_hsv,upper_hsv) # gray sacle
    # imgRes = cv2.bitwise_and(img,img,mask=mask) # with that color
    point = getContours(mask)

    if len(point) != 0:
        drawPoints.append(point)

    if len(drawPoints) != 0:
        for line in drawPoints:
            cv2.circle(applyImg,(line[0],line[1]),5, (255,0,0),cv2.FILLED)
            
            # cv2.line(canvas,(0,0),(point[0],point[1]),2)




    cv2.imshow("frame", mask)
    cv2.imshow("res", applyImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
