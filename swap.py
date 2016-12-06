import cv2
import matplotlib
import numpy as np

img = cv2.imread('images/2.jpeg')
cv2.imshow('image',img)
cv2.waitKey(0)

rows,columns,channel = img.shape

for i in range(0,rows):
	for j in range(0,(columns/2)+1):

		#swap the pixels to flip the image
		img[i,[columns-j-1,j]] = img[i,[j,columns-j-1]]

cv2.imshow('image',img)		
cv2.waitKey(0)
cv2.imwrite('2.jpg',img)
cv2.destroyAllWindows()													