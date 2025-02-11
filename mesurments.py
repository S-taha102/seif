import cv2
import cv2.aruco as aruco
import numpy as np

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_100)
detector = aruco.ArucoDetector(aruco_dict)

cap = cv2.VideoCapture(0)

aruco_real_size_cm = 5.0  

selected_points = []
pixel_per_cm = None
measurements = []

def select_points(event, x, y, flags, param):
    global selected_points, pixel_per_cm, measurements
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_points.append((x, y))
        if len(selected_points) == 2 and pixel_per_cm is not None:
            object_width_pixels = np.linalg.norm(np.array(selected_points[0]) - np.array(selected_points[1]))
            object_width_cm = object_width_pixels / pixel_per_cm
            measurements.append((selected_points[0], selected_points[1], object_width_cm))
            selected_points = []

cv2.namedWindow("ArUco Object Measurement")
cv2.setMouseCallback("ArUco Object Measurement", select_points)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = detector.detectMarkers(gray)
    
    if ids is not None:
        for i in range(len(ids)):
            c = corners[i][0]
            top_left, top_right, _, _ = c
            marker_width_pixels = np.linalg.norm(top_right - top_left)
            pixel_per_cm = marker_width_pixels / aruco_real_size_cm
            cv2.polylines(frame, [c.astype(int)], True, (0, 255, 0), 2)
            cv2.putText(frame, f"Pixel/cm: {pixel_per_cm:.2f}", (int(top_left[0]), int(top_left[1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    for pt1, pt2, width in measurements:
        cv2.line(frame, pt1, pt2, (0, 0, 255), 2)
        mid_x, mid_y = (pt1[0] + pt2[0]) // 2, (pt1[1] + pt2[1]) // 2
        cv2.putText(frame, f"Width: {width:.2f} cm", (mid_x + 10, mid_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    cv2.imshow("ArUco Object Measurement", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

