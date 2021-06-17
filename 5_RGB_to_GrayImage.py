import cv2

img = cv2.imread("image.jpg")
cv2.imshow("MY Image", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_img)

############          O R

gray_img2=cv2.imread("image.jpg",0)
cv2.imshow("Gray Image 2", gray_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()