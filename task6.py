import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal

class cam(QThread):
    updateFrame = pyqtSignal(QImage)
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        cap = cv2.VideoCapture(0)  
        while self.running:
            ret, frame = cap.read()
            if ret:
                
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                qImg = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
                self.updateFrame.emit(qImg)
        cap.release()

class Webcam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
    
      self.imageLabel = QLabel()  
      self.imageLabel.setFixedSize(600, 400)
    
      self.button = QPushButton("Stop Webcam")
      self.button.clicked.connect(self.stopwebcam)
    
    
      layout = QVBoxLayout()
      layout.addWidget(self.imageLabel)
      layout.addWidget(self.button)
      self.setLayout(layout)

    
      self.thread = cam()
      self.thread.updateFrame.connect(self.setImage)
      self.thread.start()

    def setImage(self, image):
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def stopwebcam(self):
        self.thread.stop()
        
        
app = QApplication(sys.argv)
view = Webcam()
view.show()
sys.exit(app.exec_())
