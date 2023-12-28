import cv2
print(cv2.__version__)

DisplayWidth = 640
DisplayHeight = 480

def nothing(x):
    pass

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)
cv2.namedWindow('Raw Frames')
cv2.createTrackbar('X val.', 'Raw Frames', 0, DisplayWidth, nothing)
cv2.createTrackbar('Y val.', 'Raw Frames', 0, DisplayHeight, nothing)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    ValueX = cv2.getTrackbarPos('X val.', 'Raw Frames')
    ValueY = cv2.getTrackbarPos('Y val.', 'Raw Frames')
    # print(ValueX, ValueY)
    cv2.circle(RawFrames, (ValueX, ValueY), 5, (255, 0, 0), -1)

    cv2.imshow('Raw Frames', RawFrames)
    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()