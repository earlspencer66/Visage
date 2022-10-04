#launching webcam
#launch webcam faster
#Face Detection Using OpenCV
from tokenize import Ignore
import cv2
print (cv2.__version__)
height = 480
width = 640
#frames per second
#frames_ps = 30
#object cam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

#setup facedetector
faceCascade = cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')

while True:
    Ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h = face
        #print('x=', x, 'y=', y, 'width=',w, 'height=', h)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255),3)
    #cv2.imshow('my webcam', frameGray)
    cv2.imshow('WebCam', frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1) &0xff == ord('q'):
        break
cam.release()