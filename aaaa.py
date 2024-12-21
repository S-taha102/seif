import cv2


stop_cascade = cv2.CascadeClassifier('haar_stop.xml')
yield_cascade = cv2.CascadeClassifier('haar_yield.xml')
speed_cascade = cv2.CascadeClassifier('haar_speed.xml')  

def detect_signs(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
    
    stop_signs = stop_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )
    
    
    yield_signs = yield_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30, 30)
    )

    
    speed_signs = speed_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(30, 30)
    )
    
    
    for (x, y, w, h) in stop_signs:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Stop Sign", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    
    for (x, y, w, h) in yield_signs:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, "Yield Sign", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    
    for (x, y, w, h) in speed_signs:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  
        cv2.putText(frame, "Speed Sign", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    return frame


cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = detect_signs(frame)
    cv2.imshow('Sign Detection', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
