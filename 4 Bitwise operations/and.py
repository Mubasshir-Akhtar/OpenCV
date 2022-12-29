import cv2

img1 = cv2.imread('bit image 1.png')
img2 = cv2.imread('bit image 2.png')

bit_and = cv2.bitwise_and(img1, img2, mask = None)  #Don't name the variable 'and'
#Syntax: cv2.bitwise_and(source1, source2, destination, mask)
#Parameters:
#source1: First Input Image array(Single-channel, 8-bit or floating-point)
#source2: Second Input Image array(Single-channel, 8-bit or floating-point)
#dest: Output array (Similar to the dimensions and type of Input image array)
#mask: Operation mask, Input / output 8-bit single-channel mask

cv2.imshow('Anded', bit_and)

cv2.waitKey(0)

cv2.destroyAllWindows()
