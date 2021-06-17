import cv2

img = cv2.imread("image.jpg")
cv2.imshow("original ", img)
cv2.waitKey(0)

blur = cv2.blur(img, (3,3))
cv2.imshow("Blur Image", blur)
cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Gaussian image", Gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img, 5)
cv2.imshow("median image", median)
cv2.waitKey(0)

bilateral =cv2.bilateralFilter(img, 9, 75,75)
cv2.imshow("bilateral image", bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()