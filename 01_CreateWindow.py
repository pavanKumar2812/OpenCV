import cv2
import numpy as np

print(cv2.__version__)

BlackFrame = np.zeros((250, 250, 3), np.uint8)
''' 
We are establishing a new window to display text or present the desired outcome
'''

while True:
    cv2.namedWindow("Created Frame")
    cv2.imshow("Created Frame", BlackFrame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()