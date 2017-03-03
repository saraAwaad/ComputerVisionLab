import cv2
import numpy as np

lowThreshold = 2
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
detected_edges = cv2.GaussianBlur(gray,(3,3),0)

detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)

cv2.imshow('canny demo',detected_edges)

cv2.waitKey(0)