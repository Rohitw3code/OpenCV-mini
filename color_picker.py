import cv2

cap = cv2.VideoCapture(0)
cap.set(10,20)

def empty(a):
	pass


cv2.namedWindow("HSV")
# cv2.resizedWindow("HSV",640,240)

cv2.createTrackbar("Hue Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("Sat Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)


while True:
	success , img = cap.read()
	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	h_min = cv2.getTrackbarPos("HUE Min","HSV")
	h_max = cv2.getTrackbarPos("HUE Max","HSV")
	s_min = cv2.getTrackbarPos("SAT Min","HSV")
	s_max = cv2.getTrackbarPos("SAT Max","HSV")
	v_min = cv2.getTrackbarPos("VAL Min","HSV")
	v_max = cv2.getTrackbarPos("VAL Max","HSV")

	print(h_min)

	lower = np.array([h_min,s_min,v_min])
	upper = np.array([h_max,s_max,v_max])
	mask = cv2.inRange(imgHSV,lower,upper)

	imgResult = cv2.bitwise_and(img,img,mask=mask)
	mast = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
	hstack = np.hstack([img,mask,result])

	cv2.imshow("Horizontal Stacking",hstack)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindow()
