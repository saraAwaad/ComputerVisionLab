import cv2

im=cv2.imread('hi.jpg')

img = cv2.GaussianBlur(im,(3,3),0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('original image',img)

grad_x = cv2.Sobel(gray,-1,1,0,ksize = 3, scale = 1, delta = 0,borderType = cv2.BORDER_DEFAULT)

grad_y = cv2.Sobel(gray,-1,0,1,ksize = 3, scale = 1, delta = 0,borderType = cv2.BORDER_DEFAULT)

cv2.imshow('grad_x',grad_x);
cv2.imshow('grad_y',grad_y)

dst = cv2.addWeighted(grad_x,0.5,grad_y,0.5,0)
cv2.imshow('grad_xy',dst)
cv2.waitKey(0)
