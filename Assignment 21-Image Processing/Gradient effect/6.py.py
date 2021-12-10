import cv2
import numpy as np

height = 255
width = 255

img = np.zeros((height , width) , dtype=np.uint8)

for i in range(width):

    for j in range(height):

        img[i , j] = 255 - i

cv2.imshow('255 Shades of grey' , img)

cv2.imwrite('Gradient.jpg' , img)

cv2.waitKey()