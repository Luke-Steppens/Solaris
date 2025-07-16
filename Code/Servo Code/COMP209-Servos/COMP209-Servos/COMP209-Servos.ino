#include "Servo.h"

Servo frontServo;
Servo backServo;
Servo leftServo;
Servo rightServo;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  frontServo.attach(6);
  backServo.attach(7);
  leftServo.attach(8);
  rightServo.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly:
  frontServo.write(90); // Servos work from 0 to 360 degrees.
  backServo.write(180); // Servos work from 0 to 360 degrees.
  leftServo.write(270); // Servos work from 0 to 360 degrees.
  rightServo.write(360); // Servos work from 0 to 360 degrees.

  delay(1000);  

}
