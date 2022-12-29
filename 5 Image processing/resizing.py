import cv2
import matplotlib.pyplot as plt

image = cv2.imread('glados.png')

h, w = image.shape[:2]

ratio = 1/2
dim = (int(w*ratio), int(h * ratio))

half = cv2.resize(image,dim)

bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540),
               interpolation = cv2.INTER_LINEAR)

#Fancy and honestly, shitty way to display images

Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1) #(no. of rows, no. of columns, pos of plot)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()

#Syntax: cv2.resize(source, dsize, dest, fx, fy, interpolation)
#Parameters:
#source: Input Image array (Single-channel, 8-bit or floating-point)
#dsize: Size of the output array
#dest: Output array (Similar to the dimensions and type of Input image array) [optional]
#fx: Scale factor along the horizontal axis  [optional]
#fy: Scale factor along the horizontal axis  [optional]
#interpolation: One of the above interpolation methods  [optional]

#Note: One thing to keep in mind while using the cv2.resize() function is that the tuple passed for determining the size of the new image ((1050, 1610) in this case) follows the order (width, height) unlike as expected (height, width).
