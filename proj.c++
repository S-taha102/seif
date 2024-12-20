#define cspeed 
#define forw 
#define back 
#define buzzer 

void setup() {
  Serial.begin(9600);
  pinMode(cspeed, OUTPUT);
  pinMode(forw, OUTPUT);
  pinMode(back, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String comm = Serial.readStringUntil('\n');

    if (comm == "forward") {
      digitalWrite(forw, HIGH);
      digitalWrite(back, LOW);
      analogWrite(cspeed, 10);
    } 
    else if (comm == "reverse") {
      digitalWrite(forw, LOW);
      digitalWrite(back, HIGH);
      analogWrite(cspeed, 10);
    } 
    else if (comm == "buzzer") {
      digitalWrite(buzzer, HIGH);
      delay(2000);
      digitalWrite(buzzer, LOW);
    }
  }
}