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
        HandsType=[]
        RGBFrames = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Results = self.hands.process(RGBFrames)
        if Results.multi_hand_landmarks is not None:
            print(Results.multi_hand_landmarks)
            for Hand in Results.multi_handedness:
                print(Hand)
                #print(Hand.classification)
                #print(Hand.classification[0])
                HandType=Hand.classification[0].label
                HandsType.append(HandType)
            for HandLandMarks in Results.multi_hand_landmarks:
                myHand=[]
                for LandMark in HandLandMarks.landmark:
                    myHand.append((int(LandMark.x*width),int(LandMark.y*height)))
                MyHands.append(myHand)
        return MyHands, HandsType

CameraWidth = 1280
CameraHeight = 720
Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CameraHeight)

FindHands = MediapipeMyHands(2)

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    HandData, HandsTypeData = FindHands.Marks(RawFrames, CameraWidth, CameraHeight)
    for hand,handType in zip(HandData,HandsTypeData):
        if handType=='Right':
            handColor=(255,0,0)
        if handType=='Left':
            handColor=(0,0,255)
        for ind in [0,5,6,7,8]:
            cv2.circle(RawFrames,hand[ind],15,handColor,5)
    cv2.imshow("RawFrames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()