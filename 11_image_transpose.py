import cv2

img=cv2.imread("image.jpg")
cv2.imshow("original", img)

rotated_img = cv2.transpose(img)
cv2.imshow("rotated", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()