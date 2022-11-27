#detect and recognize faces on Live WEBCAM
import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
height = 640
width = 360
#frames per second
#frames_ps = 30
#object cam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


earlFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/earl spencer.jpg')
faceLoc = FR.face_locations(earlFace)[0]
earlFaceEncoded = FR.face_encodings(earlFace)[0]

sashaFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/sasha nyaboke.jpg')
faceLoc = FR.face_locations(sashaFace)[0]
sashaFaceEncoded = FR.face_encodings(sashaFace)[0]

paulFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Paul McWhorter.jpg')
faceLoc = FR.face_locations(paulFace)[0]
paulFaceEncoded = FR.face_encodings(paulFace)[0]

knownEncodings = [earlFaceEncoded, sashaFaceEncoded, paulFaceEncoded]
names = ['Earl Spencer', 'Sasha Nyaboke', 'Paul mcWhorter']

while True:
    Ignore, unknownFace = cam.read()
    unknownFaceRGB = cv2.cvtColor(unknownFace, cv2.COLOR_RGB2BGR)
    faceLocations = FR.face_locations(unknownFaceRGB)
    unknownEncodings = FR.face_encodings(unknownFaceRGB, faceLocations)

    for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
        top, right, bottom, left = faceLocation
        print(faceLocation)
        cv2.rectangle(unknownFace, (left, top),(right, bottom), (255,0,0), 3)
        name = 'Unknown Person'
        matches =  FR.compare_faces(knownEncodings, unknownEncoding)
        print(matches)
        if True in matches:
            matchIndex = matches.index(True)
            print(matchIndex)
            print(names[matchIndex])
            name = names[matchIndex]
        cv2.putText(unknownFaceBGR, name, (left,top),font,.75, (255,0,0), 2)
    cv2.imshow('My faces', unknownFace)
#print(faceLoc)
#top, right, bottom, left = faceLoc
#cv2.rectangle(donFace, (left, top), (right, bottom),(255,0,0), 3)
#donFaceBGR=cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
#cv2.imshow('My Window', donFaceBGR)
    if cv2.waitKey(1) &0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    #gray frame 
    #grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Webcam', grayFrame)
    #cv2.moveWindow('Webcam', 100,0)
    #cv2.imshow('WebCam', frame)
    #Move window
    #cv2.moveWindow('WebCam',0,0)
    