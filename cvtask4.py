import cv2
import numpy as np

def process_coral_image(image_path, rows, cols):
    
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    white_img = np.ones_like(img) * 255

    cell_height = height // rows
    cell_width = width // cols

    
    for i in range(1, rows):
        y = i * cell_height
        cv2.line(white_img, (0, y), (width, y), (0, 0, 0), 1)
    for j in range(1, cols):
        x = j * cell_width
        cv2.line(white_img, (x, 0), (x, height), (0, 0, 0), 1)

    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])  
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    for contour in contours:
        if cv2.contourArea(contour) > 100:  
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(white_img, (center_x, center_y), 10, (0, 0, 255), -1)  

    
    cv2.imshow('Processed Coral Reef Image', white_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = 'coral-reef-1.jpg'  
rows = 8  
cols = 16  

process_coral_image(image_path, rows, cols)

