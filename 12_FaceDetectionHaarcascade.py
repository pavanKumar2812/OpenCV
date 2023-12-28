import pathlib
import cv2

CascadePath = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
# print(CascadePath)

Classifier = cv2.CascadeClassifier(str(CascadePath))

Camera = cv2.VideoCapture(0)

while True:
    Ignore, Frame = Camera.read()
    Gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    Faces = Classifier.detectMultiScale(
        Gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize = (30,30)
    )

    for (X, Y, Width, Height) in Faces:
        pt1 = (X, Y)
        pt2 = (X + Width, Y + Height)
        cv2.rectangle(Frame, pt1, pt2, (255, 255, 0), 2)

    cv2.imshow("Faces", Frame)
    if cv2.waitKey(1) == ord("q"):
        break

Camera.release()
cv2.destroyAllWindows()