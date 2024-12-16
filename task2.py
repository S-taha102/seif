import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)


fourcc = cv.VideoWriter_fourcc(*'XVID')  

def rotate_frame(frame):
    return cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)

while cap.isOpened():
    ret, frame = cap.read()
    
    

    
    cv.imshow('original Frame', frame)

    
    key = cv.waitKey(1) & 0xFF

    
    if key == ord('q'):
        break

    
    elif key == ord('c'):
        cv.imwrite('saved frame', frame)

    
    elif key == ord('s'):
        
        out = cv.VideoWriter('saved vedio', fourcc, 20.0,  (640, 480))
            
    elif key == ord('g') :
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('grayscale Frame', gray_frame)

    
    elif key == ord('h'):
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow('hsv Frame', hsv_frame)

    
    elif key == ord('r'):
        frame = rotate_frame(frame)
        cv.imshow('rotate frame',frame)

    
    elif key == ord('x'):
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        rotated_frame = rotate_frame(frame)

        
        original_resized = cv.resize(frame, (200, 200))
        gray_resized = cv.resize(cv.cvtColor(frame, cv.COLOR_BGR2GRAY), (200, 200))
        hsv_resized = cv.resize(hsv_frame, (200, 200))
        rotated_resized = cv.resize(rotated_frame, (200, 200))

        
        top_row = cv.hconcat([original_resized, cv.cvtColor(gray_resized, cv.COLOR_GRAY2BGR)])
        bottom_row = cv.hconcat([hsv_resized, rotated_resized])
        together = cv.vconcat([top_row, bottom_row])

        cv.imshow('together Frames', together)

    
cap.release()    
cv.destroyAllWindows()
