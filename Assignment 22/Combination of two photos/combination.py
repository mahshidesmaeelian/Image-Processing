import cv2
import numpy as np

img1 = cv2.imread("1.jpg" , 0)
img2 = cv2.imread("2.jpg" , 0)

img1 = cv2.resize(img1 , (450 , 450))
img2 = cv2.resize(img2 , (450 , 450))


result1 = img1//3 + img2//2
result2 = img1//2 + img2//2

cv2.imwrite('result1.jpg' , result1)
cv2.imwrite('result2.jpg' , result2)

final = np.zeros((450 , 1800) , dtype="uint8")


final[0:450 , 0:450]= img1
final[0:450 , 450:900]= result1
final[0:450 , 900:1350]= result2
final[0:450 , 1350:1800]= img2



cv2.imwrite('final_output.jpg' , final)


cv2.imshow('Combination of two photos' , final)

cv2.waitKey()