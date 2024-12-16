import numpy as np
import cv2 as cv


circles = []

def draw_circle(cr, x, y, flags, param):
    

    if cr == cv.EVENT_LBUTTONDOWN:  
        radius = 100
        color = (0, 0,255)  
        cv.circle(img, (x, y), radius, color, -1)  
        circles.append((x, y, radius, color))  

    
    cv.imshow("Image", img)

img = np.ones((500, 500, 3), np.uint8) 

cv.imshow("Image", img)
cv.setMouseCallback("Image", draw_circle)

while True:
    key = cv.waitKey(1) & 0xFF
       
    if key == ord('s'):  
        circles.clear()
        img = np.ones((500, 500, 3), np.uint8)  
        cv.imshow("Image", img)

cv.destroyAllWindows()
