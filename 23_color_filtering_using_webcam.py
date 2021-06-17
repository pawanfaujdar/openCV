import cv2
import numpy as np

device = cv2.VideoCapture(0)
while True:
    _, frame = device.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_range = np.array([110,50,50])
    upper_range = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow("show mask", mask)
    cv2.imshow("show frame", frame)

    if cv2.waitKey(1)==13:
        break

device.release()
cv2.destroyAllWindows()