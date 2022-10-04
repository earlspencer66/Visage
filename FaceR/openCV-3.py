#launching webcam
from tokenize import Ignore
import cv2
print (cv2.__version__)
height = 360
width = 640
myColor = (0,0,0)
myThickness = 2
myText = 'Earl Spencer'
#frames per second
#frames_ps = 30
#object cam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    Ignore, frame = cam.read()
    frame [140:220,250:390] =(255,0,255)
    cv2.rectangle(frame, (250,140),(390,220),(0,255,0),4)
    #cv2.circle(frame, 320,180,25,(0,0,0),2)
    cv2.putText(frame, myText, (120,60), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0 ,255),1)
    #gray frame 
    #grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Webcam', grayFrame)
    #cv2.moveWindow('Webcam', 100,0)
    cv2.imshow('WebCam', frame)
    #Move window
    #cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1) &0xff == ord('q'):
        break
cam.release()