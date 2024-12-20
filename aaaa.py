import cv2
import serial
import time

class TrafficSignDetector:
    def __init__(self, arduino_port=''):
        self.cap = cv2.VideoCapture(0)
        self.arduino = serial.Serial(arduino_port, 9600, timeout=1)
        time.sleep(2)  
        
        
        self.stop_cascade = cv2.CascadeClassifier('')
        self.speed_cascade = cv2.CascadeClassifier('')
        self.yield_cascade = cv2.CascadeClassifier('')
    
    def detect_signs(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
        stop_signs = self.stop_cascade.detectMultiScale(gray, 1.1, 5)
        speed_signs = self.speed_cascade.detectMultiScale(gray, 1.1, 5)
        yield_signs = self.yield_cascade.detectMultiScale(gray, 1.1, 5)
        
        
        if len(stop_signs) > 0:
            self.send_command('S')  
            self.draw_detection(frame, stop_signs, "Stop")
        elif len(speed_signs) > 0:
            self.send_command('F')  
            self.draw_detection(frame, speed_signs, "Speed")
        elif len(yield_signs) > 0:
            self.send_command('B')  
            self.draw_detection(frame, yield_signs, "Yield")
            
        return frame
    
    def draw_detection(self, frame, detections, label):
        for (x, y, w, h) in detections:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    def send_command(self, command):
        self.arduino.write(command.encode())
        
    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            processed_frame = self.detect_signs(frame)
            cv2.imshow('Traffic Sign Detection', processed_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        self.cap.release()
        cv2.destroyAllWindows()
        self.arduino.close()

if __name__ == "__main__":
    detector = TrafficSignDetector()
    detector.run()