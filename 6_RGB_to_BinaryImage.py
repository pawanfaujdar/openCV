import cv2

img = cv2.imread("image.jpg",0)
cv2.imshow("MY image", img)
cv2.waitKey(0)

_,bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("B&W IMAGE",bw)
cv2.waitKey(0)

cv2.destroyAllWindows()