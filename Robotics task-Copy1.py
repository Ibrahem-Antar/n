#!/usr/bin/env python
# coding: utf-8

# # Task

# In[7]:


import cv2 as cv

img = cv.imread("C:/Users/ANTER/Downloads/imgetask/Task 1 Pic.png")
cv.imshow('Before', img)

# Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", gray)

gaussianBlurImg = cv.GaussianBlur(img, (3,3) , 0)

cv.imshow("After",gaussianBlurImg)
cv.waitKey(0)


# In[8]:


import cv2 as cv

# Load the image
img = cv.imread("C:/Users/ANTER/Downloads/imgetask/nnamed.jpg")
cv.imshow('Before', img)

# Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", gray)

canny = cv.Canny(img, 50, 175)

cv.imshow('After', canny)
cv.waitKey(0)


# In[9]:


import cv2 as cv

# Load the image
img = cv.imread("C:/Users/ANTER/Downloads/imgetask/amed (1).png")
cv.imshow("Before", img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
threshold1, thresh1 = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#Adaptive Thresholding
adaptive_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
adaptive_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)



cv.imshow("Simple Threshold Image", thresh)
cv.imshow("Simple Threshold Image inv", thresh1)
cv.imshow("Adaptive Mean", adaptive_mean)
cv.imshow("Adaptive Gaussian", adaptive_gaussian)
cv.waitKey(0)


# In[ ]:




