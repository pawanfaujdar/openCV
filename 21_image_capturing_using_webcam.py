import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    _, frame = cap.read()
    print(_)
    print(frame)
else:
    _ = False
    print(_)

img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title("Camera Image")
plt.xticks([])
plt.yticks([])
plt.show()
cap.release()