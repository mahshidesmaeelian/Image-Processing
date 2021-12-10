import cv2
import numpy as np


height = 255
width = 255

img = np.zeros((height , width) , dtype=np.uint8)
img[::] = 255



img[60:70 , 80:170]= 0
img[60:130 , 80:90] = 0
img[60:130, 120:130] = 0
img[60:130, 160:170] = 0



cv2.imshow('M letter' , img)

cv2.imwrite('My initial.jpg' , img)

cv2.waitKey()