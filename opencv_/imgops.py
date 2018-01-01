import numpy as np
import cv2 

img = cv2.imread('images/mug.jpg', cv2.IMREAD_COLOR)

px = img[55,55]
print(px)

