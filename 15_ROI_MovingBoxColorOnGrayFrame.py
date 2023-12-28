import cv2
print(cv2.__version__)

DisplayWidth = 640
DisplayHeight = 480

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()

    cv2.imshow("Raw Frames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()
