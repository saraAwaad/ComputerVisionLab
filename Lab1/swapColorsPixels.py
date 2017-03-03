import cv2

#read image
im=cv2.imread('hi.jpg')

cv2.imshow('origin image',im)
#cv2.waitKey(0)

#one channel of colored image
redimage=im[:,:,0].copy()
greenimg= im[:,:,1].copy()
blueimage=im[:,:,2].copy()

#swap red and blue pixels
im[:,:,0]=blueimage
im[:,:,2]=redimage

cv2.imshow("blueimage", im)
cv2.waitKey(0)
