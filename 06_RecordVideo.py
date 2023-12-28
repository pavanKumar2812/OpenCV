import cv2
print(cv2.__version__)

DisplayWidth = 640
DisplayHeight = 480

Camera = cv2.VideoCapture(0)
Recorder = cv2.VideoWriter('media/RecordedByCV2.avi', cv2.VideoWriter_fourcc(*'XVID'), 21, (DisplayWidth, DisplayHeight))

Success, RawFrames = Camera.read()

while Success:
    Success, RawFrames = Camera.read()
    cv2.imshow('Raw Frames', RawFrames)
    cv2.moveWindow('Raw Frames', 0, 0)
    Recorder.write(RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
Recorder.release()
cv2.destroyAllWindows()