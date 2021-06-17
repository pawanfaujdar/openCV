import cv2
import numpy as np

img = cv2.imread("image.jpg")
cv2.imshow("original image", img)
cv2.waitKey(0)

img_scaled = cv2.resize(img,None, fx=0.75,fy=0.75)
cv2.imshow("scaling linear interpolation", img_scaled)
cv2.waitKey(0)

img_scaled2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.waitKey(0)

img_scaled3 = cv2.resize(img, (900,400), interpolation=cv2.INTER_AREA)
cv2.imshow("scaling - skewed size", img_scaled3)
cv2.waitKey(0)
cv2.destroyAllWindows()