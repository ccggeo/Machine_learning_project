import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainlogo.png')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2grey = cv2.cvtcolor(img2, cv2.COLOR_BG2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow(mask,'mask')

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
