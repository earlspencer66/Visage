#training models using known and unknown images
import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
earlFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/earl spencer.jpg')
faceLoc = FR.face_locations(earlFace)[0]
earlFaceEncoded = FR.face_encodings(earlFace)[0]

sashaFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/sasha nyaboke.jpg')
faceLoc = FR.face_locations(sashaFace)[0]
sashaFaceEncoded = FR.face_encodings(sashaFace)[0]

washFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Washington Kamadi.jpg')
faceLoc = FR.face_locations(washFace)[0]
washFaceEncoded = FR.face_encodings(washFace)[0]

valFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Valerian Kwamboka.jpg')
faceLoc = FR.face_locations(valFace)[0]
valFaceEncoded = FR.face_encodings(valFace)[0]

billFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/known/Bill Barr.jpg')
faceLoc = FR.face_locations(billFace)[0]
billFaceEncoded = FR.face_encodings(billFace)[0]

knownEncodings = [earlFaceEncoded, sashaFaceEncoded, washFaceEncoded, valFaceEncoded, billFaceEncoded]
names = ['Earl Spencer', 'Sasha Nyaboke', 'Washington Kamadi', 'Valerian Kwamboka', 'Bill Barr']

unknownFace = FR.load_image_file('C:/Users/earls/Documents/Visage/FaceR/demoImages/unknown/u14.jpg')
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