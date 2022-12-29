#Image erosion:
#https://buzztech.in/erosion-and-dilation-in-digital-image-processing/
#https://youtu.be/fmyE7DiaIYQ

import cv2
import numpy as np

img = cv2.imread('se1.png')

kernel = np.ones((6,6), np.uint8)  #kernel is the structuring element(in link above). u int for unsigned integer
#This np function generates unit matrix
#syntax: numpy.ones(shape, dtype=None, order='C', *, like=None)
#shape: Shape of the new array, e.g., (2, 3) or 2.
#dtype: The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.
#order: Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.
#like: Reference object to allow the creation of arrays which are not NumPy arrays.
#Returns: ndarray Array of ones with the given shape, dtype, and order

img = cv2.erode(img, kernel)
#Syntax: cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])
#Parameters:
#src: It is the image which is to be eroded .
#kernel: A structuring element used for erosion. If element = Mat(), a 3 x 3
#rectangular structuring element is used. Kernel can be created using getStructuringElement.
#dst: It is the output image of the same size and type as src.
#anchor: It is a variable of type integer representing anchor point and it’s
#default value Point is (-1, -1) which means that the anchor is at the kernel center.
#borderType: It depicts what kind of border to be added. It is defined by flags
#like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc.
#iterations: It is number of times erosion is applied.
#borderValue: It is border value in case of a constant border.
#Return Value: It returns an image.

cv2.imshow('Eroded', img)

cv2.waitKey(0)
