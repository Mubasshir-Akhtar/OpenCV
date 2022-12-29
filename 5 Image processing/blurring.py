#Important types of blurring:

#Gaussian Blurring: Gaussian blur is the result of blurring an image by a Gaussian
#function. It is a widely used effect in graphics software, typically to reduce
#image noise and reduce detail. It is also used as a preprocessing stage before
#applying our machine learning or deep learning models.

#Median Blur: The Median Filter is a non-linear digital filtering technique,
#often used to remove noise from an image or signal. Median filtering is very
#widely used in digital image processing because, under certain conditions, it
#preserves edges while removing noise. It is one of the best algorithms to remove
#Salt and pepper noise.

#Bilateral Blur: A bilateral filter is a non-linear, edge-preserving, and
#noise-reducing smoothing filter for images. It replaces the intensity of each
#pixel with a weighted average of intensity values from nearby pixels.
#This weight can be based on a Gaussian distribution. Thus, sharp edges are
#preserved while discarding the weak ones.

#More about Gaussian blurring:
#https://aryamansharda.medium.com/image-filters-gaussian-blur-eb36db6781b1#

import cv2

image = cv2.imread("se1.png")

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)
#Syntax: cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType=BORDER_DEFAULT]]] )
#src	input image
#dst	output image
#ksize	Gaussian Kernel Size. [height width]. height and width should be odd and
#can have different values. If ksize is set to [0 0], then ksize is computed from sigma values.
#sigmaX	Kernel standard deviation along X-axis (horizontal direction).
#sigmaY	Kernel standard deviation along Y-axis (vertical direction). If sigmaY=0, then sigmaX value is taken for sigmaY
#borderType	Specifies image boundaries while kernel is applied on image borders.
#Possible values are : cv.BORDER_CONSTANT cv.BORDER_REPLICATE cv.BORDER_REFLECT
#cv.BORDER_WRAP cv.BORDER_REFLECT_101 cv.BORDER_TRANSPARENT cv.BORDER_REFLECT101
#cv.BORDER_DEFAULT cv.BORDER_ISOLATED


# Median Blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)
#Syntax: medianBlur(src, dst, ksize)
#src − A Mat object representing the source (input image) for this operation.
#dst − A Mat object representing the destination (output image) for this operation.
#ksize − A Size object representing the size of the kernel.


# Bilateral Blur
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Syntax: bilateralFilter(src, dst, d, sigmaColor, sigmaSpace, borderType)
#src − A Mat object representing the source (input image) for this operation.
#dst − A Mat object representing the destination (output image) for this operation.
#d − A variable of the type integer representing the diameter of the pixel neighborhood.
#sigmaColor − A variable of the type integer representing the filter sigma in the color space.
#sigmaSpace − A variable of the type integer representing the filter sigma in the coordinate space.
#borderType − An integer object representing the type of the border use
