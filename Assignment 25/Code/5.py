import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret,frame = video_capture.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    camera = frame[150:300,250:400]
      
    if ret == False:
        break
 
    kernel = np.ones((35,35),np.float32)/1225
    dst = cv2.filter2D(frame,-1,kernel)

    dst[150:300,250:400] = camera
    color_detection_area = dst[150:300,250:400]

    if  0 < np.average(color_detection_area) <= 60:
        cv2.putText(dst, "Black", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 
    elif 70 < np.average(color_detection_area) <= 120:
        cv2.putText(dst, "Gray", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    else:
        cv2.putText(dst, "White", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 

    cv2.imshow('Camera',dst)
    cv2.waitKey(1)   