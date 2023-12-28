import cv2
print(cv2.__version__)
import numpy as np

def MousePoints(event, x, y, flags, params):
    global counter, circles, matrix, width, height
    if event == cv2.EVENT_LBUTTONDOWN and counter < 4:
        circles[counter] = x, y
        counter += 1
        print(circles)
        if counter == 4:
            width = int(np.linalg.norm(circles[0] - circles[1]))
            height = int(np.linalg.norm(circles[0] - circles[2]))

            pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)

def main():
    global counter, circles, matrix, width, height

    DisplayWidth = 640
    DisplayHeight = 480

    Camera = cv2.VideoCapture(0)
    Camera.set(cv2.CAP_PROP_FRAME_WIDTH, DisplayWidth)
    Camera.set(cv2.CAP_PROP_FRAME_HEIGHT, DisplayHeight)

    circles = np.zeros((4, 2), int)
    counter = 0

    cv2.namedWindow("Raw Video")
    cv2.setMouseCallback("Raw Video", MousePoints)

    Success, RawFrames = Camera.read()
    while Success:
        Success, NextFrame = Camera.read()

        for x in range(0, 4):
            cv2.circle(NextFrame, (circles[x][0], circles[x][1]), 3, (0, 255, 0), cv2.FILLED)

        # Move the following lines inside the loop
        if counter == 4:
            AreaOfInterest = cv2.warpPerspective(NextFrame, matrix, (width, height))
            cv2.imshow("Area of Interest", AreaOfInterest)

        cv2.imshow("Raw Video", NextFrame)

        if cv2.waitKey(1) == ord('q'):
            break

    Camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()