// Pin assignments for motor control
int forwardPin = 9;  // Pin for moving forward (motor control)
int reversePin = 10; // Pin for moving backward (motor control)
int buzzerPin = 11;  // Pin for the buzzer

void setup() {
  // Initialize motor and buzzer pins as outputs
  pinMode(forwardPin, OUTPUT);
  pinMode(reversePin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  
  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();  // Read the incoming character
    
    // Stop sign detected (Reverse)
    if (receivedChar == 'S') {
      moveBackward();   // Move backward (Reverse)
      stopMoving();     // Ensure both motors stop after reversing
    }
    
    // Speed sign detected (Move Forward)
    else if (receivedChar == 'P') {
      moveForward();    // Move forward
      stopMoving();     // Ensure both motors stop after moving forward
    }
    
    // Yield sign detected (Activate Buzzer)
    else if (receivedChar == 'Y') {
      turnBuzzer();     // Turn on buzzer
    }
  }
}

// Function to move forward (motor control)
void moveForward() {
  digitalWrite(forwardPin, HIGH);  // Turn on motor for moving forward
  digitalWrite(reversePin, LOW);   // Turn off motor for reverse
}

// Function to move backward (reverse)
void moveBackward() {
  digitalWrite(forwardPin, LOW);   // Turn off motor for moving forward
  digitalWrite(reversePin, HIGH);  // Turn on motor for reverse
}

// Function to stop both motors
void stopMoving() {
  digitalWrite(forwardPin, LOW);   // Turn off forward motor
  digitalWrite(reversePin, LOW);   // Turn off reverse motor
}

// Function to turn on the buzzer
void turnBuzzer() {
  digitalWrite(buzzerPin, HIGH);   // Turn on buzzer
  delay(1000);                     // Keep it on for 1 second
  digitalWrite(buzzerPin, LOW);    // Turn off buzzer
}
