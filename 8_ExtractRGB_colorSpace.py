import cv2
import numpy as np

img = cv2.imread("image.jpg")
cv2.imshow("Original", img)
cv2.waitKey(0)

B,G,R = cv2.split(img)
zeroes = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("RED", cv2.merge([zeroes,zeroes,R]))
cv2.waitKey(0)

cv2.imshow("Green", cv2.merge([zeroes,G,zeroes]))
cv2.waitKey(0)

cv2.imshow("Blue", cv2.merge([B,zeroes,zeroes]))
cv2.waitKey(0)

cv2.destroyAllWindows()