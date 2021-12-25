import argparse
import cv2
import matplotlib.pyplot as plt
import imutils
from imutils import contours
from imutils.perspective import four_point_transform


parser = argparse.ArgumentParser(description= "Mahshid Sudoku detector v 1.0 ")
parser.add_argument("--input" , type=str , help = "enter the path of your image" )
parser.add_argument("--filter-size" , type=int , help = "enter the size ofGaussianBlur mask" , default = 7 )
parser.add_argument("--output" , type=str , help = "enter the path of your output image")
args = parser.parse_args()


img = cv2.imread(args.input)
img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

blurred_img = cv2.GaussianBlur(img_gray , (args.filter_size , args.filter_size ) , 3)
plt.imshow(blurred_img , cmap="gray")



threshold = cv2.adaptiveThreshold(blurred_img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2)
plt.imshow(threshold , cmap="gray")


threshold = cv2.bitwise_not(threshold)
plt.imshow(threshold , cmap="gray")


contours = cv2.findContours(threshold , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0]

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
    result = cv2.drawContours(img , [sudoku_contour] , -1 ,(0,255,0) , 8)
    result2 = four_point_transform(img, sudoku_contour.reshape(4,2))
    warped = four_point_transform(img_gray, sudoku_contour.reshape(4,2))
    cv2.imshow("Result" ,result2)
    cv2.imwrite(args.output, result2)





