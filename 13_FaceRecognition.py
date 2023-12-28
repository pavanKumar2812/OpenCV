import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX

CameraWidth=640
CameraHeight=360
Camera=cv2.VideoCapture(0)
Camera.set(cv2.CAP_PROP_FRAME_WIDTH, CameraWidth)
Camera.set(cv2.CAP_PROP_FRAME_HEIGHT,CameraHeight)

donFace=FR.load_image_file('media/Pavan.png')
faceLoc=FR.face_locations(donFace)[0]
PavanFaceEncode=FR.face_encodings(donFace)[0]

knownEncodings=[PavanFaceEncode]
names=['Pavan Kumar A']

while True:
    ignore,  unknownFace = Camera.read()
 
    unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
    faceLocations=FR.face_locations(unknownFaceRGB)
    unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)
 
    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        print(faceLocation)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)
        name='Unknown Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            print(matchIndex)
            print(names[matchIndex])
            name=names[matchIndex]
        cv2.putText(unknownFace,name,(left,top),font,.75,(0,0,255),2)
 
    cv2.imshow('My Faces',unknownFace)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
Camera.release()
cv2.destroyAllWindows()