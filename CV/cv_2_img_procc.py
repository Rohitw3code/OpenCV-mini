import cv2
import random as rd
import numpy as np


cap = cv2.VideoCapture(0)
f = [cv2.COLOR_BGR2HSV][0]
while True:
    success, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
#    cv2.imshow('mask', mask)
    cv2.imshow('res', res)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
