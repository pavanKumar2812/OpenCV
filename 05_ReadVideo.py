import cv2
print(cv2.__version__)

VideoFile = cv2.VideoCapture('./media/TomJerry.mp4')

Success, Frames = VideoFile.read()
while Success:
    Success, Frames = VideoFile.read()
    cv2.imshow('Tom & Jerry', Frames)

    if cv2.waitKey(1) == ord('q'):
        break

VideoFile.release()
cv2.destroyAllWindows()