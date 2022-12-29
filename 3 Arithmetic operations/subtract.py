# Python program to illustrate
# arithmetic operation of
# subtraction of pixels of two images

# organizing imports
import cv2
import os
import numpy as np

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# cv2.subtract is applied over the
# image inputs with applied parameters
sub = cv2.subtract(image1, image2)

# the window showing output image
# with the subtracted image
cv2.imshow('Subtracted Image', sub)
directory = r'C:\Users\mubas\onedrive\desktop\image\test'
os.chdir(directory)
cv2.imwrite("Demonic.jpg", sub)

# De-allocate any associated memory usage
if cv2.waitKey(0):
	cv2.destroyAllWindows()
