import cv2
print(cv2.__version__)

Camera = cv2.VideoCapture(0)
Font = cv2.FONT_HERSHEY_DUPLEX

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    RawFrames = cv2.rectangle(RawFrames, (340, 100), (400, 170), (255, 0, 0),4)
    RawFrames = cv2.circle(RawFrames, (400, 400), 50, (255, 0, 255), -1 )
    RawFrames = cv2.putText(RawFrames, "Namaste :)", (300, 300), Font, 1, (255, 0, 150), 2)
    RawFrames = cv2.line(RawFrames, (10, 10), (450, 600), (255, 255, 255), 4)
    RawFrames = cv2.arrowedLine(RawFrames, (10, 470), (630, 10), (0, 0, 0), 2)
    cv2.imshow('Raw Frames', RawFrames)
    cv2.moveWindow('Raw Frames', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()