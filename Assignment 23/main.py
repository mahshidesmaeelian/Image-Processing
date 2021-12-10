import cv2

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

colorful_img = cv2.imread("1.jpg")
gray_img = cv2.imread("1.jpg" , 0)
# img = cv2.resize(gray_img , (0,0) , fx=0.5 , fy=0.5)

faces = face_detector.detectMultiScale(gray_img , 1.3 , minSize = (100 , 100))

for face in faces:
    x , y , w , h = face
    cv2.rectangle(colorful_img , (x , y) , (x+w , y+h) , (0 , 255 , 0) , 5)


cv2.imshow('output' , colorful_img)
cv2.waitKey()