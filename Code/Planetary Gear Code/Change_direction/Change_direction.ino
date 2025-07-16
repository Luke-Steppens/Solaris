#include <EEPROM.h>

const int enA = 5;       // PWM pin for motor speed
const int in1 = 10;      // IN1
const int in2 = 9;       // IN2
const int eepromAddress = 0;  // Where to store last direction

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  // Read last direction from EEPROM
  byte lastDirection = EEPROM.read(eepromAddress);
  bool forward = (lastDirection == 0);  // flip it

  // Write the opposite for next time
  EEPROM.write(eepromAddress, forward ? 1 : 0);

  // Set motor direction
  if (forward) {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  } else {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  }

  // speed up 5 seconds
  for (int speed = 50; speed <= 255; speed += 5) {
    analogWrite(enA, speed);
    delay(100);  // 5 seconds total
  }

  // max speed 50 seconds
  analogWrite(enA, 255);
  delay(50000);

  //  slow Down 5 seconds
  for (int speed = 255; speed >= 50; speed -= 5) {
    analogWrite(enA, speed);
    delay(100);  // 5 seconds total
  }

  // Stop the motor
  analogWrite(enA, 0);
}

void loop() {
  // Do nothing
}
