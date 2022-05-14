import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(10,100)


while True:
	success , img = cap.read()
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	face = faceCascade.detectMultiScale(imgGray,1.1,4)
	for (x,y,w,h) in face:
		cv2.rectangle(imgGray,(x,y),(x+w,y+h),(255,0,0),2)


	cv2.imshow("video1",imgGray)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break



# cv2.imshow("oggy",img)
# cv2.waitKey(0)