
int forwardPin = 9;  
int reversePin = 10; 
int buzzerPin = 11;  

void setup() {
  
  pinMode(forwardPin, OUTPUT);
  pinMode(reversePin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();  
    
    
    if (receivedChar == 'S') 
      moveBackward();   
      stopMoving();     
    }
    
    
    else if (receivedChar == 'P') {
      moveForward();    
      stopMoving();     
    }
    
    
    else if (receivedChar == 'Y') {
      turnBuzzer();     
    }
  }
}


void moveForward() {
  digitalWrite(forwardPin, HIGH);  
  digitalWrite(reversePin, LOW);   
}


void moveBackward() {
  digitalWrite(forwardPin, LOW);   
  digitalWrite(reversePin, HIGH);  
}


void stopMoving() {
  digitalWrite(forwardPin, LOW);   
  digitalWrite(reversePin, LOW);   
}


void turnBuzzer() {
  digitalWrite(buzzerPin, HIGH);   
  delay(1000);                     
  digitalWrite(buzzerPin, LOW);    
