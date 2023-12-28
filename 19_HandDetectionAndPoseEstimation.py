import cv2
print(cv2.__version__)
import mediapipe as mp

CameraWidth = 1280
CameraHeight = 720

Camera = cv2.VideoCapture(0)

Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CameraHeight)

Hands = mp.solutions.hands.Hands(static_image_mode=False, 
                                max_num_hands=2, 
                                min_detection_confidence=0.5, 
                                min_tracking_confidence=0.5)

mpDraw = mp.solutions.drawing_utils

Success, RawFrames = Camera.read()
while Success:
    myHands = []
    Success, RawFrames = Camera.read()
    # RawFrames = cv2.resize(RawFrames, (640, 480))
    RGBFrames = cv2.cvtColor(RawFrames, cv2.COLOR_BGR2RGB)
    Results = Hands.process(RGBFrames)
    print(Results)
    if Results.multi_hand_landmarks is not None:
        for HandLandMarks in Results.multi_hand_landmarks:
            myHand = []
            # print(HandLandMarks)
            mpDraw.draw_landmarks(RawFrames, HandLandMarks, mp.solutions.hands.HAND_CONNECTIONS)
            for LandMark in HandLandMarks.landmark:
                # print(LandMark.x, LandMark.y, LandMark.z)
                myHand.append((int(LandMark.x * CameraWidth), int(LandMark.y * CameraHeight)))
            print("")
            # cv2.circle(RawFrames, myHand[17], 15, (255, 0, 255), -1)
            # cv2.circle(RawFrames, myHand[18], 15, (255, 0, 255), -1)
            # cv2.circle(RawFrames, myHand[19], 15, (255, 0, 255), -1)
            # cv2.circle(RawFrames, myHand[20], 15, (255, 0, 255), -1)
            myHands.append(myHand)
            print(myHands)
    cv2.imshow("RawFrames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()
