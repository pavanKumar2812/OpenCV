import cv2
print(cv2.__version__)

CameraWidth = 640
CameraHeight = 360

Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CameraHeight)

FaceCascade = cv2.CascadeClassifier("XML/haarcascade_frontalface_default.xml")

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    
    GrayFrames = cv2.cvtColor(RawFrames, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("GrayFrames", GrayFrames)

    Faces = FaceCascade.detectMultiScale(GrayFrames, scaleFactor=1.3, minNeighbors=5)
    # print(Faces)
    for Face in Faces:
        x,y,w,h = Face
        print(f"x= {x}, y= {y}, width= {w}, height= {h}")
        cv2.rectangle(RawFrames, (x,y), (x+w, y+h), (255, 0, 0))

    cv2.imshow("RawFrames", RawFrames)
    
    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()