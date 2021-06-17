import cv2
import numpy as np

img = cv2.imread("image.jpg")
# height, width = img.shape

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("original image", img)
cv2.waitKey(0)

cv2.imshow("sobel x image", sobel_x)
cv2.waitKey(0)

cv2.imshow("sobel y image", sobel_y)
cv2.waitKey(0)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow(" sobel Or", sobel_OR)
cv2.waitKey(0)

lapcian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow("Lapcian image", lapcian)
cv2.waitKey(0)

canny = cv2.Canny(img, 20, 170)
cv2.imshow("Canny Edge", canny)
cv2.waitKey(0)

cv2.destroyAllWindows()