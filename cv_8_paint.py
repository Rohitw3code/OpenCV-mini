import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(10, 20)

myColors = [[48, 0, 255, 109, 255, 255]]
myColorValues = [[51,153,255]] # BGR
myPoints = [] # x,y,colorId

def findColor(img, myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for col in myColors:
        lower = np.array(col[0:3])
        upper = np.array(col[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10,myColorValues[count], cv2.FILLED)
        count+=1
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        # cv2.imshow(str(col[0]), mask)
    return newPoints

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0],point[1]), 10,myColorValues[0], cv2.FILLED)

def getContours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            # cv2.putText(imgResult,"Pen Cap",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
    return x+w//2,y


while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("video1", imgResult)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# cv2.imshow("oggy",img)
# cv2.waitKey(0)