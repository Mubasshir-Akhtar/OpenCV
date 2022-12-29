import cv2

image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

added = cv2.addWeighted(image1, 0.5, image2, 0.2, 0)
#Performs the weighted sum of the image pixels
#Input parameters are Input image 1, weight of pixels of image 1, input image 2,
#weight of pixels of image 2, gamma factor
# O = (I/255)^(1/gamma) * 255
#where I - input pixel value (0 to 255), O - output pixel value (0 to 255)
#gamma <1 darker image, gamma >1 lighter image

cv2.imshow('Weighted Image',added)
cv2.waitKey(0)
cv2.destroyAllWindows()
