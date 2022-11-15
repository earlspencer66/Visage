#training models using known and unknown images
import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
donFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Donald Trump.jpg')
faceLoc = FR.face_locations(donFace)[0]
donFaceEncoded = FR.face_encodings(donFace)[0]

nancyFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Nancy Pelosi.jpg')
faceLoc = FR.face_locations(nancyFace)[0]
nancyFaceEncoded = FR.face_encodings(nancyFace)[0]

paulFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Paul McWhorter.jpg')
faceLoc = FR.face_locations(paulFace)[0]
paulFaceEncoded = FR.face_encodings(paulFace)[0]

penceFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Mike Pence.jpg')
faceLoc = FR.face_locations(penceFace)[0]
penceFaceEncoded = FR.face_encodings(penceFace)[0]

billFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Bill Barr.jpg')
faceLoc = FR.face_locations(billFace)[0]
billFaceEncoded = FR.face_encodings(billFace)[0]

knownEncodings = [donFaceEncoded, nancyFaceEncoded, paulFaceEncoded, penceFaceEncoded, billFaceEncoded]
names = ['Donald Trump', 'Nancy Pelosi', 'Paul mcWhorter', 'Mike Pence', 'Bill Barr']

unknownFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/unknown/u5.jpg')
unknownFaceBGR = cv2.cvtColor(unknownFace, cv2.COLOR_RGB2BGR)
faceLocations = FR.face_locations(unknownFace)
unknownEncodings = FR.face_encodings(unknownFace, faceLocations)

for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
    top, right, bottom, left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR, (left, top),(right, bottom), (255,0,0), 3)
    name = 'Unknown Person'
    matches =  FR.compare_faces(knownEncodings, unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex = matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name = names[matchIndex]
    cv2.putText(unknownFaceBGR, name, (left,top),font,.75, (255,0,0), 2)
cv2.imshow('My faces', unknownFaceBGR)
#print(faceLoc)
#top, right, bottom, left = faceLoc
#cv2.rectangle(donFace, (left, top), (right, bottom),(255,0,0), 3)
#donFaceBGR=cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
#cv2.imshow('My Window', donFaceBGR)
cv2.waitKey(5000)