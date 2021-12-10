import cv2

img = cv2.imread('2.jpg' , 0)
print(img)


height , width = img.shape


img[::] = 255 - img[::]

            

cv2.imshow('reversed color effect' , img)

cv2.imwrite('result2.jpg' , img)

cv2.waitKey()