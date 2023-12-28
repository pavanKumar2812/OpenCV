import cv2
import numpy as np 
import time

print(cv2.__version__)

Width=720
Height=480
Font=cv2.FONT_HERSHEY_SIMPLEX

Camera1=cv2.VideoCapture(0)
Camera2=cv2.VideoCapture(1)

while True:
    ignore, frame1 = Camera1.read()
    ignore, frame2 = Camera2.read()
    frame3 = np.hstack((frame1, frame2))
    cv2.imshow('Combo Camera', frame3)
    if cv2.waitKey(1) == ord('q'):
        break

Camera1.release()
Camera2.release()
cv2.destroyAllWindows()