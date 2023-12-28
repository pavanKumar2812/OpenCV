import cv2
import numpy as np
print(cv2.__version__)

Font = cv2.FONT_HERSHEY_PLAIN
PointArr = []
EventStatus = -1

BlackWindow = np.zeros((250, 250, 3), np.uint8)

def click(event, x, y, flags, params):
    global Point 
    global EventStatus
    if event == cv2.EVENT_LBUTTONDOWN:
        Point = (x, y)
        PointArr.append(Point)
        EventStatus = event
        # In opencv pixel color values are in a tuple (blue, green, red)
        # Normally we assume that x for rows and y for columns but in this case we pass first y and x values  
        Blue = RawFrames[y, x, 0]
        Green = RawFrames[y, x, 1]
        Red = RawFrames[y, x, 2]
        print(Blue, Green, Red)
        ColorStr = str(Blue) + "," + str(Green) + "," + str(Red)
        BlackWindow[:] = [Blue, Green, Red]
        # If the window is became the picked color then the text should be contrast color so we do this
        r = 255 - int(Red)
        b = 255 - int(Blue)
        g = 255 - int(Green)
        TextColorTuple = (b, g, r)
        cv2.putText(BlackWindow, ColorStr, (10, 25), Font, 1, TextColorTuple, 2)
        cv2.imshow("My Color", BlackWindow)

DisplayWidth = 640
DisplayHeight = 480

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    for Points in PointArr:
        cv2.circle(RawFrames, Points, 5, (0, 0, 255), -1)
        PointStr = str(Points)
        cv2.putText(RawFrames, PointStr, Points, Font, 1.5, (255, 0, 0), 2)
    cv2.imshow("Raw Frames", RawFrames)
    cv2.moveWindow("Raw Frames", 0, 0)
    cv2.setMouseCallback("Raw Frames", click)

    KeyEvent = cv2.waitKey(1)
    if KeyEvent == ord('q'):
        break

    if KeyEvent == ord('c'):
        PointArr = []

Camera.release()
cv2.destroyAllWindows()
