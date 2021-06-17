import cv2
import numpy as np

img = cv2.imread("image.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)

kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel_sharpening)
cv2.imshow("image sharping", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()