import cv2
import numpy as np
import time
print(cv2.__version__)
TimeMark=time.time()
dtFIL=0
 
def nothing(x):
    pass

width=720
height=480
flip=2
font=cv2.FONT_HERSHEY_SIMPLEX

cam1=cv2.VideoCapture(0)
cam2=cv2.VideoCapture(1)

cv2.namedWindow('TrackBars')
# cv2.moveWindow('TrackBars',1320,0)
cv2.createTrackbar('hueLower', 'TrackBars',0,179,nothing)
cv2.createTrackbar('hueUpper', 'TrackBars',179,179,nothing)
cv2.createTrackbar('satLow', 'TrackBars',0,255,nothing)
cv2.createTrackbar('satHigh', 'TrackBars',255,255,nothing)
cv2.createTrackbar('valLow', 'TrackBars',0,255,nothing)
cv2.createTrackbar('valHigh', 'TrackBars',255,255,nothing)

while True:
    _, frame1 = cam1.read()
    _, frame2 = cam2.read()

    hsv1=cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    hsv2=cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)
 
    hueLow=cv2.getTrackbarPos('hueLower', 'TrackBars')
    hueUp=cv2.getTrackbarPos('hueUpper', 'TrackBars')
 
    Ls=cv2.getTrackbarPos('satLow', 'TrackBars')
    Us=cv2.getTrackbarPos('satHigh', 'TrackBars')
 
    Lv=cv2.getTrackbarPos('valLow', 'TrackBars')
    Uv=cv2.getTrackbarPos('valHigh', 'TrackBars')
 
    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])
 
    FGmask1=cv2.inRange(hsv1,l_b,u_b)
    FGmask2=cv2.inRange(hsv2,l_b,u_b)
 
    cv2.imshow('FGmask1',FGmask1)
    # cv2.moveWindow('FGmask1',0,0)
 
    contours1,_ = cv2.findContours(FGmask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours1=sorted(contours1,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours1:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=100:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,255),3)
            break
    
    contours2,_ = cv2.findContours(FGmask2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours2=sorted(contours2,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours2:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=100:
            cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,255),3)
            break
 
    frame3=np.hstack((frame1,frame2))
    dt=time.time()-TimeMark
    TimeMark=time.time()
    dtFIL=.9*dtFIL + .1*dt
    fps=1/dtFIL
    cv2.rectangle(frame3,(0,0),(150,40),(0,0,255),-1)
    cv2.putText(frame3,'fps: '+str(round(fps,1)),(0,30),font,1,(0,255,255),2)
 
    #cv2.imshow('myCam1',frame1)
    #cv2.imshow('myCam2',frame2)
    cv2.imshow('comboCam',frame3)
    # cv2.moveWindow('comboCam',0,450)
    if cv2.waitKey(1)==ord('q'):
        break
cam1.release()
cam2.release()
cv2.destroyAllWindows()