import serial
import serial.tools.list_ports

def findport():
    ports = list(serial.tools.list_ports.comports())  #
    for port in ports:
     return None

def connectarduino(port):
    return serial.Serial(port, 9600, timeout=1)  

def port():
    arduinoport = findport()

    arduino = connectarduino(arduinoport)

    while True:
        user_input = input("Enter 1 to turn LED, 0 to turn OFF LED ")
        
        if user_input == '1':
            arduino.write('1') 
        elif user_input == '0':
            arduino.write('0')  
        elif user_input == 'exit':
            break  
        
    arduino.close()  
    if __name__ == '__main__':
      port()
