import cv2
import numpy as np

im=cv2.imread('median.jpg')

kernel=np.zeros((9,9),np.float32)
kernel[4][7]=1

print kernel
#kernel=kernel/81
#im2=cv2.filter2D(im,-1,kernel,borderType = cv2.BORDER_CONSTANT)

#im2=cv2.blur(im,(9,9))
#im2=cv2.GaussianBlur(im, (9,9), 1.7)

im2= cv2.medianBlur(im,9)

cv2.imshow('im',im)
cv2.imshow('im2',im2)
cv2.waitKey(0)


