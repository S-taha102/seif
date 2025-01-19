import cv2 as cv

face=cv.CascadeClassifier('face.xml')

def detect(frame):
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    face_detect=face.detectMultiScale(gray,scaleFactor=1.1,
        minNeighbors=3)
    
    for(x,y,w,h) in face_detect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    return frame
cap = cv.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    ssframe = detect(frame)
    cv.imshow('Sign Detection', ssframe)

    if cv.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv.destroyAllWindows()
