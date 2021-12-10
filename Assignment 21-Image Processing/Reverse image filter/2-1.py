import cv2

img = cv2.imread('1.jpg' , 0)
print(img)


height , width = img.shape


img[::] = 255 - img[::]

            

cv2.imshow('reversed color effect' , img)

cv2.imwrite('result1.jpg' , img)

cv2.waitKey()