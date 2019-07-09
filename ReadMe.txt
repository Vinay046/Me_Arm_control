MeArm Control

This project focuses on developing an user interface for the control of the MeArm. The MeArm is an open Source robotic platform.
The primary focus is on developing a mathematical model of the given robot and then developing an application that communicates with the microcontroller in order to control the robot.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
********************************************************************************************   Version 1   **************************************************************************************************************
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This iteration consists:-
- GUI which offers control for 3 servo angles and one button to toggle the grabber
- The angles generated on the GUI are packed in a string and sent to the micro-controller via a serial port
- The angles are parsed from the string received from the PC
- Corresponding functions are executed based on the string received.