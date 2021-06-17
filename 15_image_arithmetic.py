import cv2
import numpy as np
img = cv2.imread("image.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)

M = np.ones(img.shape, dtype="uint8")*150
M1 = np.zeros(img.shape, dtype="uint8")+150

added = cv2.add(img, M1)
cv2.imshow("added", added)

subtract = cv2.subtract(img, M1)
cv2.imshow("substract", subtract)

mul = cv2.multiply(img, M1)
cv2.imshow("multiply ", mul)

cv2.waitKey(0)
cv2.destroyAllWindows()