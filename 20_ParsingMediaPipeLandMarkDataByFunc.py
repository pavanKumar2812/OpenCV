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

def ParseLandMark(Frame):
    myHands = []
    RGBFrames = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
    Results = Hands.process(RGBFrames)
    if Results.multi_hand_landmarks is not None:
        for HandLandMarks in Results.multi_hand_landmarks:
            myHand = []
            for LandMark in HandLandMarks.landmark:
                # print(LandMark.x, LandMark.y, LandMark.z)
                myHand.append((int(LandMark.x * CameraWidth), int(LandMark.y * CameraHeight)))
            # print("")
            myHands.append(myHand)
            # print(myHands)
    return myHands

Success, RawFrames = Camera.read()
while Success:
    Success, RawFrames = Camera.read()
    myHands = ParseLandMark(RawFrames)
    for hand in myHands:
        # cv2.circle(RawFrames, hand[20], 15, (255, 0, 255), 3)
        for dig in [8, 12, 16, 20]:
            cv2.circle(RawFrames, hand[dig], 15, (255, 0, 255), 3)
    cv2.imshow("RawFrames", RawFrames)

    if cv2.waitKey(1) == ord('q'):
        break

Camera.release()
cv2.destroyAllWindows()
