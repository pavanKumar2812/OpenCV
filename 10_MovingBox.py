import cv2
print(cv2.__version__)

DisplayWidth = 640
DisplayHeight = 480

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)

DisplayWidth = int(Camera.get(cv2.CAP_PROP_FRAME_WIDTH))
DisplayHeight = int(Camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"W: {DisplayWidth}, H: {DisplayHeight}")
RectangleWidth = int(.15 * DisplayWidth)
RectangleHeight = int(.25 * DisplayHeight)
RectangleX = 10
RectangleY = 270
IncrementValueX = 2
IncrementValueY = 2 

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    Rectangle = cv2.rectangle(RawFrames, (RectangleX, RectangleY), (RectangleX + RectangleWidth, RectangleY + RectangleHeight), (255, 0, 0),-1)
    cv2.imshow("Rectangle", Rectangle)
    RectangleX = RectangleX + IncrementValueX
    RectangleY = RectangleY + IncrementValueY

    if RectangleX <= 0 or RectangleX + RectangleWidth >= DisplayWidth:
        IncrementValueX = IncrementValueX * (-1)
    
    if RectangleY <= 0 or RectangleY + RectangleHeight >= DisplayHeight:
        IncrementValueY = IncrementValueY * (-1)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()