import cv2

#read image
im=cv2.imread('hi.jpg')
#h,w=im.shape[:2]
#print h,w
height, width, channels = im.shape
print height, width, channels
print 'Helllo'
#save the result
cv2.imwrite('result11.jpg',im)
cv2.imshow('flood fill2',im)
#cv2.waitKey(0)

#crop image
crop_img = im[100:300, 100:200] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
h,w=crop_img.shape[:2]
print h,w
cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)


#one channel of colored image
redimage=im[:,:,0]
greenimg= im[:,:,1]
blueimage=im[:,:,2]

cv2.imshow("redimage", redimage)
cv2.imshow("greenimg", greenimg)
cv2.imshow("blueimage", blueimage)
cv2.waitKey(0)
