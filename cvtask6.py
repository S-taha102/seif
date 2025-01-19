import cv2
import numpy as np

def measure_object(image_path, reference_length_cm):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array([20, 100, 100])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    def onclick(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            global points, reference_pixels, is_reference_set
            points.append((x, y))
            cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
            
            if len(points) == 2:
                pixel_distance = np.sqrt((points[1][0] - points[0][0])**2 + 
                                      (points[1][1] - points[0][1])**2)
                
                if not is_reference_set:
                    reference_pixels = pixel_distance
                    is_reference_set = True
                    cv2.line(img, points[0], points[1], (255, 0, 0), 2)
                    cv2.putText(img, f'{reference_length_cm:.1f}', 
                              (int((points[0][0] + points[1][0])/2), 
                               int((points[0][1] + points[1][1])/2)),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                else:
                    distance_cm = (pixel_distance * reference_length_cm) / reference_pixels
                    cv2.line(img, points[0], points[1], (0, 255, 0), 2)
                    cv2.putText(img, f'{distance_cm:.1f}', 
                              (int((points[0][0] + points[1][0])/2), 
                               int((points[0][1] + points[1][1])/2)),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                points.clear()
            cv2.imshow('Image', img)
    
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', onclick)
    
    global points, reference_pixels, is_reference_set
    points = []
    reference_pixels = None
    is_reference_set = False
    
    
    
    
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

reference_length_cm = float(input("Enter the reference length : "))
measure_object('image2.jpeg', reference_length_cm)