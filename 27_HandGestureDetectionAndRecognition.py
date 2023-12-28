import cv2
print(cv2.__version__)
import numpy as np

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

def FindDistances(HandLandMarks):
    DistanceMatrix = np.zeros([len(HandLandMarks), len(HandLandMarks)], dtype="float")
    for row in range(0, len(HandLandMarks)):
        for column in range(0, len(HandLandMarks)):
            DistanceMatrix[row, column] = ((HandLandMarks[row][0]-HandLandMarks[column][0])**2 + (HandLandMarks[row][1]-HandLandMarks[column][1])**2 )**(1./2.)       
    return DistanceMatrix

def FindError(GestureMatrix, UnknownMatrix, KeyPoints):
    Error = 0
    for row in KeyPoints:
        for column in KeyPoints:
            Error = Error + abs(GestureMatrix[row][column] - UnknownMatrix[row][column])
    return Error

CameraWidth = 1280
CameraHeight = 720
Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CameraHeight)

FindHands = MediapipeMyHands(1)
Font = cv2.FONT_HERSHEY_COMPLEX

KeyPoints = [0, 4, 5, 9, 13, 17, 8, 12, 16, 20]
Train = True

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    HandData = FindHands.Marks(RawFrames, CameraWidth, CameraHeight)
    if Train == True:
        if HandData is not None:
            print("Show your Gesture, Press t when Ready")
            if cv2.waitKey(1) & 0xff == ord('t'):
                KnownGesture = FindDistances(HandData[0])
                Train = False
                print(KnownGesture)
    if Train == False:
        if HandData is not None:
            UnknownGesture = FindDistances(HandData[0])
            Error = FindError(KnownGesture, UnknownGesture, KeyPoints)
            cv2.putText(RawFrames, str(int(Error,)), (100, 175), Font, 3, (255, 0, 0), 6)

    for hand in HandData:
        for i in range(21):
            cv2.circle(RawFrames, hand[i], 5, (255, 0, 255), 3)
    cv2.imshow("RawFrames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()