import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

	_, frame = cap.read()
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)   	
	sobelx = cv2.Sobel(frame,cv2.CV_64F, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame,cv2.CV_64F, 0, 1, ksize=5)
	edges = cv2.Canny(frame, 100, 100)

	grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#blur = cv2.GaussianBlur(img,(5,5),0)
	
	gausian = cv2.GaussianBlur(grayscale, (5,5),100)	
	
	sobelgal = cv2.Sobel(gausian,cv2.CV_64F, 1, 0, ksize=5)
	
		
	cv2.imshow('original', frame)
	#cv2.imshow('laplacian', laplacian)
	cv2.imshow('sobelx', sobelx)
	#cv2.imshow('sobely', sobely)
	cv2.imshow('gausian', gausian)
	cv2.imshow('sobelgal', sobelgal)
	#cv2.imshow('edges', edges) 	

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
