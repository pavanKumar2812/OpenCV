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
IndexFingerDot = 8
PaddleWidth = 125
PaddleHeight = 25
PaddleColor = (255, 0, 0)

BallX = 640
BallY = 360
BallRadius = 25
IncrementValueX = 10
IncrementValueY = 10
Score = 0
Lives = 5
Font = cv2.FONT_HERSHEY_COMPLEX

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    cv2.circle(RawFrames, (BallX, BallY), BallRadius, (0, 0, 255), -1)
    cv2.putText(RawFrames, str(Score), (25, int(6* PaddleHeight)), Font, 1, (0, 0, 255), 4)
    cv2.putText(RawFrames, str(Lives), (CameraWidth - 125, int(6 * PaddleHeight)), Font, 1, (0, 0, 255), 4)
    HandData = FindHands.Marks(RawFrames, CameraWidth, CameraHeight)
    for hand in HandData:
        cv2.rectangle(RawFrames, (int(hand[8][0] - PaddleWidth/2), 0), (int(hand[8][0]+ PaddleWidth), PaddleHeight), PaddleColor, -1)
    BallX = BallX + IncrementValueX
    BallY = BallY + IncrementValueY
    TopEdgeBall = BallY - BallRadius
    BottomEdgeBall = BallY + BallRadius
    LeftEdgeBall = BallX - BallRadius
    RightEdgeBall = BallX + BallRadius
    if LeftEdgeBall <= 0 or RightEdgeBall >= CameraWidth:
        IncrementValueX = IncrementValueX * (-1)
    if BottomEdgeBall >= CameraHeight:
        IncrementValueY = IncrementValueY * (-1)
    if TopEdgeBall <= PaddleHeight:
        if BallX >= int(hand[IndexFingerDot][0] - PaddleWidth/2) and BallX <= int(hand[IndexFingerDot][0] + PaddleWidth/2):
            IncrementValueY = IncrementValueY * (-1)
            Score += 1
        else:
            Lives -= 1
            BallX = int(CameraWidth / 2)
            BallY = int(CameraHeight / 2)
    cv2.imshow("RawFrames", RawFrames)
    if cv2.waitKey(1) == ord('q'):
        break
    if Lives == 0:
        BallX = int(CameraWidth / 2)
        BallY = int(CameraHeight / 2)
        IncrementValueX = 0
        IncrementValueY = 0
Camera.release()
cv2.destroyAllWindows()
