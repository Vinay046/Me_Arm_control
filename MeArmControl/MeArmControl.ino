#include<Servo.h>
String inData;
int angle1,angle2,angle3;
String ang1,ang2,ang3;
String state;
Servo base,left,right,grabber;
void setup() 
{
  base.attach(5);
  base.write(90);
  
  left.attach(6);
  left.write(0);
  
  right.attach(9);
  right.write(9);
  
  grabber.attach(10);
  grabber.write(0);
  
  Serial.begin(9600);
}
void loop()
{
  
  while (Serial.available() > 0)
  {
    char recieved = Serial.read();
    inData += recieved;   
    if (recieved == '!')
    {
      if(inData[0]=='@')
      {
        int index1 = inData.indexOf(',',1);
        angle1 = (inData.substring(1,index1)).toInt();
        int index2 = inData.indexOf(',',index1+1);
        angle2 = (inData.substring(index1+1,index2+1)).toInt();
        int index3 = inData.indexOf(',',index2+1);
        angle3 = (inData.substring(index2+1,index3+1)).toInt();
        int index4 = inData.indexOf(',',index3+1);
        state = (inData.substring(index3+1,inData.indexOf('!')));   
        base.write(angle1);
        left.write(angle2);
        right.write(angle3);
        if(state == "Release")
        {
          grabber.write(123);   
        }
        else
        {
          grabber.write(70);
        }
      }
      inData = "";
    }
  }
}
