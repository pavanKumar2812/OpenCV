import cv2
print(cv2.__version__)

EventStatus = -1 
Font = cv2.FONT_HERSHEY_PLAIN
PointsArr = []

def click(event, x, y, flags, params):
    global Point 
    global EventStatus  
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event was: ', event)
        print(x, ',', y)
        Point = (x, y)
        PointsArr.append(Point)
        EventStatus = event

DisplayWidth = 640
DisplayHeight = 480

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    for Points in PointsArr:
        cv2.circle(RawFrames, Points, 5, (0, 0, 255), -1)
        PointStr = str(Points)
        cv2.putText(RawFrames, PointStr, Points, Font, 1.5, (255, 0, 0), 2)
    cv2.imshow("Raw Frames", RawFrames)
    cv2.moveWindow('Raw Frames', 0, 0)
    cv2.setMouseCallback('Raw Frames', click)
    
    KeyEvent = cv2.waitKey(1)
    if KeyEvent == ord('q'):
        break

    if KeyEvent == ord('c'):
        PointsArr = []

Camera.release()
Camera.destroyAllWindows()