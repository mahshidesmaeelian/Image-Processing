import cv2
import numpy as np


width = 800
height = 800
chessboard = np.zeros((height , width) , dtype=np.uint8)

board = chessboard[::] = 255
pattern = chessboard[0:100 , 0:100] = 0

for i in range(0 , width , 200):

    for j in range(0 , height , 200):
    
        chessboard[i:i+100 , j:j+100] = pattern


for i in range(100 , width , 200):

    for j in range(100 , height , 200):
        
        chessboard[i:i+100 , j:j+100] = pattern



cv2.imshow('chessboard' , chessboard)

cv2.imwrite('chessboard.jpg' , chessboard)

cv2.waitKey()