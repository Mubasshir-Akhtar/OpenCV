import cv2

image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

added = cv2.add(image1,image2)  #Function that adds two images

cv2.imshow('Test',added)
cv2.waitKey(0)

#Image should be of equal size and depth
