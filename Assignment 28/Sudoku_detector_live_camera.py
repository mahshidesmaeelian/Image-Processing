import argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils
from imutils import contours
from imutils.perspective import four_point_transform

camera_frame = cv2.VideoCapture(0)

while True:
    ret,frame = camera_frame.read()
    if not ret:
        break

    camera_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    blurred_img = cv2.GaussianBlur(camera_frame_gray , (3,3), 3)
    plt.imshow(blurred_img , cmap="gray")



    threshold = cv2.adaptiveThreshold(blurred_img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2)
    plt.imshow(threshold , cmap="gray")


    threshold = cv2.bitwise_not(threshold)
    plt.imshow(threshold , cmap="gray")


    contours = cv2.findContours(threshold , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours , key = cv2.contourArea , reverse = True)


    sudoku_contour = None

    for contour in contours :
        
        epsilon = 0.02 * cv2.arcLength(contour , True)
        approx = cv2.approxPolyDP(contour , epsilon , True)
                                
        if len(approx) == 4:
            sudoku_contour = approx 
            break
            
    if sudoku_contour is None:
        print("couldn't find the sudoku table")

    else:
        result = cv2.drawContours(frame , [sudoku_contour] , -1 ,(0,255,0) , 5)

    cv2.imshow("Live Camera", frame)

    if cv2.waitKey(1) == ord('s'):
        if sudoku_contour is None :
            print("couldn't find the sudoku table")
        else:
            result2 = four_point_transform(frame, sudoku_contour.reshape(4,2))
            warped = four_point_transform(camera_frame_gray, sudoku_contour.reshape(4,2))
            cv2.imwrite("Sudoku.jpg" , result2)

    if cv2.waitKey(1) == ord('q'):
        break





