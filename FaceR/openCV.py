#launching webcam
from tokenize import Ignore
import cv2
print (cv2.__version__)
#object cam
cam = cv2.VideoCapture(0)
while True:
    Ignore, frame = cam.read()
    #gray frame 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Webcam', grayFrame)
    #cv2.moveWindow('Webcam', 100,0)
    cv2.imshow('WebCam', frame)
    #Move window
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1) &0xff == ord('q'):
        break
cam.release()