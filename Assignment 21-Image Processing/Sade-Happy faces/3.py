import cv2

img = cv2.imread('3.jpg' , 0)

img = cv2.resize(img , (940 , 720))

print(img.shape)

rotate_image = img[::-1 ,::-1]

cv2.imshow('rotated image' , rotate_image)

cv2.imwrite('happy men.jpg' , rotate_image)

cv2.waitKey()