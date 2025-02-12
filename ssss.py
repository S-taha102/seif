import cv2
import numpy as np


MARKER_SIZE_CM = 5.0


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100)
parameters = cv2.aruco.DetectorParameters()


points = []
pixels_cm = None

def click_event(event, x, y, flags, param):
    global points, pixels_per_cm

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

        if len(points) == 2 and pixels_per_cm is not None:
            
            pixel_distance = np.linalg.norm(np.array(points[0]) - np.array(points[1]))
            # Convert to real-world distance (cm)
            distance_cm = pixel_distance / pixels_per_cm
            print(f"Measured Distance: {distance_cm:.2f} cm")

            
            cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
            cv2.circle(frame, points[0], 5, (0, 0, 255), -1)
            cv2.circle(frame, points[1], 5, (0, 0, 255), -1)
            mid_x, mid_y = (points[0][0] + points[1][0]) // 2, (points[0][1] + points[1][1]) // 2
            cv2.putText(frame, f"{distance_cm:.2f} cm", (mid_x, mid_y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            points.clear()  


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        
        marker_width_pixels = np.linalg.norm(corners[0][0][0] - corners[0][0][1])
        pixels_per_cm = marker_width_pixels / MARKER_SIZE_CM

    
    cv2.imshow("Measurement", frame)
    cv2.setMouseCallback("Measurement", click_event)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
