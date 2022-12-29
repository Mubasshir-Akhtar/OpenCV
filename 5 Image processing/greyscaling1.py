#Method 1: Using cvtColor function

import cv2

img = cv2.imread('se1.png')

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()
