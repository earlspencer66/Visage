#launching webcam
#understanding Region of Interest (ROI) in OpenCV
from tokenize import Ignore
import cv2
print (cv2.__version__)
height = 360
width = 640
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
    frameROI = frame[150:210,250:390]
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    cv2.imshow('my ROI',frameROI)
    cv2.moveWindow('my ROI', 650,0)
    cv2.imshow('my gray ROI', frameROIGray)
    cv2.moveWindow('my gray ROI', 650,90)
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