import cv2
import numpy as np

widthImage = 640
heightImage = 480

cap = cv2.VideoCapture(0)
cap.set(10, 150)

# img = cv2.imread("page.webp")
# img = cv2.resize(img,(widthImage,heightImage))

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            # cv2.drawContours(imgCount, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgCount, biggest, -1, (255, 0, 0), 20)
    return biggest


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)
    return imgThres

def getWarp(img,biggest):
    pass


# imgThres = preProcessing(img)

# cv2.imshow("thres",imgThres)
# cv2.imshow("page",img)

# cv2.waitKey(0)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (widthImage, heightImage))

    imgCount = img.copy()

    imgThres = preProcessing(img)

    biggest = getContours(imgThres)
    getWarp(img,biggest)


    cv2.imshow("count", imgCount)
    cv2.imshow("thres", imgThres)
    cv2.imshow("page", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
