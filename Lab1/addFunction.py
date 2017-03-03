import cv2

img1=cv2.imread('pics/4.1.01.tiff')  #('gray1.bmp')
img2=cv2.imread('gray1.bmp')  #('gray3.jpg')

h1,w1=img1.shape[:2]
print h1,w1

h2,w2=img2.shape[:2]
print h2,w2

newimg= img2[0:h1,0:w1]
cv2.imshow("im1", img1)
cv2.imshow("im2", newimg)

summedImg= img1+newimg

cv2.imshow("summed", summedImg)
cv2.waitKey(0)