import cv2
print(cv2.__version__)

class MediapipeMyHands():
    import mediapipe as mp
    def __init__(self, maxHands = 2, tol1 = .5, tol2 = .5):
        self.hands = self.mp.solutions.hands.Hands(
                                                    static_image_mode=False, 
                                                    max_num_hands=maxHands, 
                                                    min_detection_confidence=tol1, 
                                                    min_tracking_confidence=tol2
                                                )
        
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

class MediapipePose:
    import mediapipe as mp

    def __init__(self, still=False, upperBody=False, smoothData=True, tol1=0.5, tol2=0.5):
        self.myPose = self.mp.solutions.pose.Pose(
            static_image_mode=still,
            smooth_landmarks=smoothData,
            min_detection_confidence=tol1,
            min_tracking_confidence=tol2
        )

        if not still:
            self.myPose._upper_body_only = upperBody

    def Marks(self,frame, width, height):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark: 
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks

class MediaPipeFace:
    import mediapipe as mp
    
    def __init__(self):
        self.MyFace = self.mp.solutions.face_detection.FaceDetection()
    
    def Marks(self, frame, width, height):
        RGBFrames = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Results = self.MyFace.process(RGBFrames)
        FaceBoundingBoxs = []
        if Results.detections is not None:
            for Face in Results.detections:
                BoundingBox = Face.location_data.relative_bounding_box
                TopLeft = (int(BoundingBox.xmin * width), int(BoundingBox.ymin * height))
                BottomRight = (int((BoundingBox.xmin + BoundingBox.width) * width), int((BoundingBox.ymin + BoundingBox.height) * height))
                FaceBoundingBoxs.append((TopLeft, BottomRight))
        return FaceBoundingBoxs

CameraWidth = 1280
CameraHeight = 720
Camera = cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CameraHeight)
Font = cv2.FONT_HERSHEY_COMPLEX
FontColor = (255, 0, 0)

FindHands = MediapipeMyHands(2)
FindFace = MediaPipeFace()
FindPose = MediapipePose()

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    HandLandMarks, HandsTypeData = FindHands.Marks(RawFrames, CameraWidth, CameraHeight)
    for hand,handType in zip(HandLandMarks,HandsTypeData):
        if handType == "Right":
            Label = "Right"
        if handType == "Left":
            Label = "Left"
        cv2.putText(RawFrames, Label, hand[8], Font, 2, FontColor, 2)

    FaceLocation = FindFace.Marks(RawFrames, CameraWidth, CameraHeight)
    for Face in FaceLocation:
        cv2.rectangle(RawFrames, Face[0], Face[1], (255, 0, 0), 3)
    
    PoseLandmarks = FindPose.Marks(RawFrames, CameraWidth, CameraHeight)
    if PoseLandmarks is not None and len(PoseLandmarks) >= max([13, 14, 15, 16]) + 1:
        for index in [13, 14, 15, 16]:
            cv2.circle(RawFrames, PoseLandmarks[index], 20, (0, 255, 0), -1)


    cv2.imshow("RawFrames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()
