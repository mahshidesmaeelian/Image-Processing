import cv2
import numpy as np

img = cv2.imread("Tae.jpeg" , 0)

inverted = 255 - img
bluerred = cv2.GaussianBlur(inverted , (21 , 21) , 0)
inverted_blurred = 255 - bluerred
sketch = img/inverted_blurred
sketch = sketch * 255

cv2.imshow('s' , sketch)

cv2.imwrite('painting.jpg' , sketch)


cv2.waitKey() 

