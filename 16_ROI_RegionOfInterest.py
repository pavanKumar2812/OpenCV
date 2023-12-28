import cv2
print(cv2.__version__)

DisplayWidth = 640
DisplayHeight = 480

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    # ROI = RawFrames[50:250,200:400] // if we didn't use the copy of the frame the ROI also became white when we set the RawFrames to white
    ROI = RawFrames[50:250,200:400].copy()
    # print(ROI.shape)
    ROIGray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
    ROIGray = cv2.cvtColor(ROIGray, cv2.COLOR_GRAY2BGR)
    RawFrames[50:250,200:400] = ROIGray

    cv2.imshow("Raw Frames", RawFrames)
    cv2.moveWindow("Raw Frames", 0, 0)
    cv2.imshow("ROI", ROI)
    cv2.moveWindow("ROI",650,0)
    cv2.imshow("ROIGray", ROIGray)
    cv2.moveWindow("ROIGray",650,200)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()