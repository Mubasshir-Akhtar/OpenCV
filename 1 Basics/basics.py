# Importing the OpenCV library
import cv2
import os #Importing image libarary for later use
# Reading the image using imread() function
image = cv2.imread('image.png')             #Like storing the file handle

# Extracting the height and width of an image
h, w = image.shape[:2]
#Has 3 parameters; height, width and channel (RGB/BW/etc.)
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))
# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
(B, G, R) = image[100, 100]

# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

# We will calculate the region of interest
# by slicing the pixels of the image
# roi = image[100 : 500, 200 : 700]
#This does not preserve aspect ratio of the image.
#To preserve it, we have to do the following

# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)

# Calculating the center of the image
center = (w // 2, h // 2)

# Generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0) #(centre, angle, scaling factor)
#Because the image is just a matrix of RGB values, the transformation
#of rotation can be done by multiplying with the rotation matrix
#Here, we generate the rotation matrix

# Performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w, h))
#An affine transformation is a general transformation involving
#rotation, translation, isometric scaling and shearing.
#For more info, check PDFs that I've saved or check the following link
#https://www.quora.com/In-an-intuitive-explanation-what-is-an-affine-transformation-of-image

#Displaying the image
cv2.imshow("window_name", rotated)
#Takes two parameters, name of the window in which the image is shown
#and the name of the file to be shown

cv2.waitKey(0)
#It takes a single argument, which is the time (in milliseconds),
#for which the window will be displayed.
#If the user presses any key within this time period, the program continues.
#If 0 is passed, the program waits indefinitely for a keystroke.

#Making a rectangle
# We are copying the original image,
# as it is an in-place operation.
output = image.copy()
#An in-place operation is an operation that changes directly the content
#of a given Tensor without making a copy.

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (255, 0, 0), 2)
#It takes in 5 arguments
#Image, Top-left corner co-ordinates, Bottom-right corner co-ordinates
#Color (in BGR format), Line width

cv2.imshow("Test1", rectangle)
cv2.waitKey(0)

# Copying the original image
output = image.copy()

# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (500, 550),
				cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
#It takes in 7 arguments
#Image, Text to be displayed
#Bottom-left corner co-ordinates, from where the text should start
#Font, Font size, Color (BGR format), Line width

cv2.imshow("Test2", text)
cv2.waitKey(0)

cv2.destroyAllWindows()
# It is for removing/deleting created GUI window from screen
# and memory

import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("image.png")

# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Displaying image using plt.imshow() method
plt.imshow(img)

#Saving an image in a path
image_path = r'C:\Users\mubas\onedrive\desktop\image\image.png'
# Image directory
directory = r'C:\Users\mubas\onedrive\desktop\image\test'
# Using cv2.imread() method to read the image
img = cv2.imread(image_path)
# Change the current directory to specified directory
os.chdir(directory)
# List files and directories
# in 'C:/Users/mubas\onedrive\desktop\image'
print("Before saving image:")
print(os.listdir(directory))
# Filename
filename = 'savedImage.jpg'
# Using cv2.imwrite() method for saving the image
cv2.imwrite(filename, img)
# List files and directories in 'C:/Users /mubas\onedrive\desktop\image\test'
print("After saving image:")
print(os.listdir(directory))
print('Successfully saved')
