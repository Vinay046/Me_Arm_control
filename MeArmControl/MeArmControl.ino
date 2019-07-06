#include<Servo.h>

Servo middle,left,right,grabber;

void setup()
{
  Serial.begin(9600);
  middle.attach(5);
  left.attach(6);
  right.attach(9);
  grabber.attach(10);
}
void loop()
{
  middle.write();
  left.write();
  right.write();
  grabber.write();
  delay(2000):
}
