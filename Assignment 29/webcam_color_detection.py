import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)

while True:

    ret,frame = video_capture.read()
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    camera = frame[150:300,250:400]
      
    if ret == False:
        break
 
    kernel = np.ones((35,35),np.float32)/1225
    dst = cv2.filter2D(frame,-1,kernel)

    dst[150:300,250:400] = camera
    color_detection_area = dst[150:300,250:400]

    b = color_detection_area[:, :, :1]
    g = color_detection_area[:, :, 1:2]
    r = color_detection_area[:, :, 2:]
    
    blue_mean = np.mean(b)
    green_mean = np.mean(g)
    red_mean = np.mean(r)
  
    if blue_mean>150 and green_mean<50 and red_mean<50:
        cv2.putText(frame, "Blue", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (255, 0, 0) ,3) 

    elif blue_mean<50 and green_mean<50 and red_mean>150:
        cv2.putText(frame, "Red", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (0, 0, 255) ,3) 
    
    elif blue_mean<50 and green_mean>150 and red_mean<50:
        cv2.putText(frame, "Green", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (0, 255, 0) ,3) 

    elif blue_mean>180 and green_mean>180 and red_mean>180:
        cv2.putText(frame, "White", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (255, 255, 255) ,3) 

    elif blue_mean>150 and green_mean>150 and red_mean<50:
        cv2.putText(frame, "Cyan", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (255, 255, 0) ,3) 
    
    elif blue_mean>150 and green_mean<50 and red_mean>150:
        cv2.putText(frame, "Magenta", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (255, 0 , 255) ,3) 

    elif blue_mean<50 and green_mean>150 and red_mean>150:
        cv2.putText(frame, "Yellow", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (0 , 255, 255) ,3) 
    
    elif blue_mean<50 and green_mean<50 and red_mean<50:
        cv2.putText(frame, "Black", (25, 50), cv2.FONT_HERSHEY_PLAIN , 3 , (0 , 0 , 0) ,3) 

    else: 
        cv2.putText(dst, "Color out of range!", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
        #cv2.putText(dst, "Sorry!This color detector dosent support the current color!", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)

    cv2.imshow('Camera' , dst)
    cv2.waitKey(1)   


