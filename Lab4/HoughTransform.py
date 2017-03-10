import cv2
import numpy as np

img = cv2.imread('ps1-input1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

def hough_transform(edges):
	# Rho and Theta ranges
	thetas = np.deg2rad(np.arange(-90.0, 90.0))
	width, height = gray.shape
	diag_len = np.ceil(np.sqrt(width * width + height * height))   # max_dist
	rhos = np.linspace(-diag_len, diag_len, diag_len * 2.0)

	# Cache some resuable values
	cos_t = np.cos(thetas)
	sin_t = np.sin(thetas)
	num_thetas = len(thetas)

	# Initialize Hough accumulator array of theta vs rho
### put your code here
	
	# Vote algorithm in the hough accumulator
###		put your code here
					
					
	return accumulator, thetas, rhos
	
accumulator, thetas, rhos = hough_transform(edges)




# Easiest peak finding based on max votes
idx = np.argmax(accumulator)
rho = rhos[idx / accumulator.shape[1]]
theta = thetas[idx % accumulator.shape[1]]
print "rho={0:.2f}, theta={1:.0f}".format(rho, np.rad2deg(theta))

