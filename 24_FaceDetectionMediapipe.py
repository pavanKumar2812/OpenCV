import cv2
print(cv2.__version__)
import mediapipe as mp

CameraWidth = 1280
CameraHeight = 720
Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CameraHeight)

FindFaces = mp.solutions.face_detection.FaceDetection()
DrawFaces = mp.solutions.drawing_utils

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    RGBFrames = cv2.cvtColor(RawFrames, cv2.COLOR_BGR2RGB)
    Results = FindFaces.process(RGBFrames)
    # print(Results.detections)
    if Results.detections is not None:
        for Face in Results.detections:
            # print(Face)
            # DrawFaces.draw_detection(RawFrames, Face)
            BoundingBox = Face.location_data.relative_bounding_box
            TopLeft = (int(BoundingBox.xmin * CameraWidth), int(BoundingBox.ymin * CameraHeight))
            BottomRight = (int((BoundingBox.xmin + BoundingBox.width) * CameraWidth), int((BoundingBox.ymin + BoundingBox.height) * CameraHeight))
            cv2.rectangle(RawFrames, TopLeft, BottomRight, (255, 0, 0), 3)
    cv2.imshow("Frames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()