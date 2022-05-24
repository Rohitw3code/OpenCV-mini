import cv2
import numpy as np
import random as rd

cap = cv2.VideoCapture(0)

drawPoints = []
font = cv2.FONT_HERSHEY_SIMPLEX


def getContours(img):
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, w, h = 0, 0, 0, 0
    center = (0,0)
    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)
        # cv2.drawContours(canvas, cnt, -1, (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)), 3)
        epsilon = 0.1*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        x, y, w, h = cv2.boundingRect(approx)

        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])        

        # center = (x+w//2, y+h//2)
        center = (cX,cY)
        cv2.circle(applyImg, center, 8, (0, 0, 255), -1)
        # cv2.circle(applyImg, center, 80-rd.randint(0, 30), (235, 201, 52))
        # cv2.putText(applyImg,"Red",(x,y),font,2,(0,0,0),2,cv2.LINE_AA)
        # cv2.rectangle(applyImg,(x,y),(x+w,y+h),(0,255,0),3)

    return center


pre = (0, 0)
canvas = np.zeros((550, 550, 3), np.uint8)*255

while True:
    success, img = cap.read()
    frame = cv2.flip(img, 1)
    imgRes = frame.copy()
    # create canvas
    applyImg = canvas

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    kernel = np.ones((5, 5), np.uint8)
    lower_hsv = np.array([50, 100, 100])
    upper_hsv = np.array([90, 255, 255])
    # lower_hsv = np.array([64,117,177])
    # upper_hsv = np.array([174,185,255])

    mask = cv2.inRange(imgHsv, lower_hsv, upper_hsv)  # gray sacle
    mask = cv2.dilate(mask, kernel, iterations=1)
    # imgRes = cv2.bitwise_and(img,img,mask=mask) # with that color
    point = getContours(mask)

    if pre != 0:
        cX = point[0]
        cY = point[1]
        cv2.line(canvas, pre, (cX, cY), (0, 0, 255), 10)
        pre = (cX, cY)

    cv2.imshow("frame", mask)
    cv2.imshow("res", canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
