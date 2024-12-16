import serial
import serial.tools.list_ports
import time


def findport():
    ports = list(serial.tools.list_ports.comports())  
    


def connectarduino(port):
    return serial.Serial(port, 9600, timeout=1)  


def port():
    arduinoport = findport()

    

    arduino = connectarduino(arduinoport)
    

    
    while True:
        if arduino.in_waiting > 0:
            button_state = arduino.readline().decode('utf-8').strip()  
            if button_state == '1':
                print("Button Press")
            else:
                print("Button Releas")
        time.sleep(1)  

    arduino.close()  

if __name__ == '__main__':
    port()
