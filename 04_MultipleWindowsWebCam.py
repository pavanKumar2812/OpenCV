import cv2
print(cv2.__version__)

Camera = cv2.VideoCapture(0)  # If it does not work, try setting to '1' instead of '0'

Success, Frame = Camera.read()
while Success:
    Success, Frame = Camera.read()
    cv2.imshow('Raw Frames',Frame)
    cv2.moveWindow('Raw Frames', 0, 0)

    GrayFrames = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Frames', GrayFrames)
    cv2.moveWindow('Gray Frames', 630, 0)
    if cv2.waitKey(1)==ord('q'):
        break
Camera.release()
cv2.destroyAllWindows()