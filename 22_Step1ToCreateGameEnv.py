import cv2
print(cv2.__version__)

class MediapipeMyHands():
    import mediapipe as mp
    def __init__(self, maxHands = 2, tol1 = .5, tol2 = .5):
        self.hands = self.mp.solutions.hands.Hands(static_image_mode=False, 
                                                    max_num_hands=maxHands, 
                                                    min_detection_confidence=tol1, 
                                                    min_tracking_confidence=tol2)
        
    def Marks(self, frame, width, height):
        MyHands = []
        RGBFrames = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Results = self.hands.process(RGBFrames)
        if Results.multi_hand_landmarks is not None:
            for HandLandMarks in Results.multi_hand_landmarks:
                MyHand = []
                for LandMark in HandLandMarks.landmark:
                    MyHand.append((int(LandMark.x * width), int(LandMark.y * height)))
                MyHands.append(MyHand)
        return MyHands

CameraWidth = 1280
CameraHeight = 720
Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CameraHeight)

FindHands = MediapipeMyHands()
PaddleWidth = 125
PaddleHeight = 25
PaddleColor = (255, 0, 0)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    HandData = FindHands.Marks(RawFrames, CameraWidth, CameraHeight)
    for hand in HandData:
        cv2.rectangle(RawFrames, (int(hand[8][0] - PaddleWidth/2), 0), (int(hand[8][0]+ PaddleWidth), PaddleHeight), PaddleColor, -1)
    cv2.imshow("RawFrames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()
