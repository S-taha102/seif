import cv2 as cv
import serial

stop=cv.CascadeClassifier('.git/haar_stop.xml')
speed = cv.CascadeClassifier('.git/haar_speed.xml')
yeild=cv.CascadeClassifier('.git/haar_yield.xml')

arduino=serial.Serial('',9600)

cap=cv.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    stopsign=stop.detectMultiScale(1.1,4)
    speedsign=speed.detectMultiScale(1.1,4)
    yeildsign=yeild.detectMultiScale(1.1,4)
    
    if len(stopsign)>0:
        print('stop sign detect')
        arduino.write(b'reverse\n')
    elif len(speedsign)>0:
        print('speed sign move forward')    
        arduino.write(b'forward\n')
    elif len(yeildsign)>0:
        print('yeild sign detected')    
        arduino.write(b'buzzer\n')
    cv.imshow('cam',frame)
    
    



    cap.release()
    cv.destroyAllWindows()

      
    


