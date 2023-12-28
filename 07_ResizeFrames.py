import cv2
print(cv2.__version__)

DisplayWidth = 960
DisplayHeight = 720

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    cv2.imshow('Raw Frames', RawFrames)
    cv2.moveWindow('Raw Frames', 630, 0)

    GrayFrames = cv2.cvtColor(RawFrames, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Frames', GrayFrames)
    cv2.moveWindow('Gray Frames', 0, 0)

    RawFrameSmall = cv2.resize(RawFrames, (320, 240))
    GrayFrameSmall = cv2.resize(GrayFrames, (320, 240))
    cv2.imshow('Raw Frames Small', RawFrameSmall)
    cv2.imshow('Gray Frames Small', GrayFrameSmall)
    cv2.moveWindow('Gray Frames Small', 350, 500)
    cv2.moveWindow('Raw Frames Small', 0, 500)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows() 
