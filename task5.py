import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout

class Calc(QWidget):
    def __init__(self,):
        super().__init__()
        self.initUi()
    def initUi(self):
        box=QVBoxLayout()
        self.display=QLineEdit()  
        self.display.setStyleSheet("font size")
        box.addWidget(self.display)
        grid=QGridLayout()
        buttons=[('7',0,0),('8',0,1),('9',0,2),('/',0,3),('4',1,0),('5',1,1),('6',1,2),('X',1,3),('1',2,0),('2',2,1),('3',2,2),('-',2,3),('0',3,0),('c',3,1),('=',3,2),('+',3,3)]
        
        for num,row,column in buttons:
            button=QPushButton(num)
            button.setStyleSheet("font size")
            grid.addWidget(button,row,column)
        box.addLayout(grid)    
        self.setLayout(box)
        self.setGeometry(200, 200, 300, 300)
        self.show()
        

app = QApplication(sys.argv)
calculator = Calc()
sys.exit(app.exec_())
            
            
            
        