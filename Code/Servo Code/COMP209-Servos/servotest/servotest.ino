#include "Servo.h"
int pinb =  9;
int pint = 10;
Servo motor1;
Servo motor2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  motor1.attach(pinb);
  motor2.attach(pint);
}

void loop() {
  // put your main code here, to run repeatedly:
  motor1.write(90);
  motor2.write(90);
  increase(0);
  decrease(180);
  position(10);
  position(100);
}

void increase(int i) {
  for(i; i < 180; i++)
  {
    motor1.write(i);
    motor2.write(i);
    delay(10);
  }
}

void decrease(int i){
  for (i; i > 0; i++)
  {
    motor1.write(i);
    motor2.write(i);
    delay(10);
  }
}
void position(int i){
  motor1.write(i);
  motor2.write(i);
}
