
//#include <SoftwareSerial.h>
#include <avr/sleep.h> 

//-=-=-=-=-=-=-=-=-=-=-=-=-= Pins allocation
// On NANO pins 3, 5, 6, 9, 10, 11 are PWM pins 490 Hz (pins 5 and 6: 980 Hz)

#define interruptPin 3 // On NANO, pin D2 and D3 are interupt enabled pins
#define MotorPin 2
#define DirectionPin 6

//const byte MotorPin = 2, DirectionPin = 6; 

//-=-=-=-=-=-=-=-=-=-=-=-=-= COMMS
float outMsg[3], inMsg[1];
char OutgoingIdentifier[2];

//-=-=-=-=-=-=-=-=-=-=-=-=-= FLAGS
int DropWeightFlag = 0;

//-=-=-=-=-=-=-=-=-=-=-=-=-= GENERAL
unsigned long PreviousMillisIn = 0, PreviousMillisOut = 0;
unsigned long HBwait = 20000; // Wait time (in milliseconds)
unsigned long MotorTime = 20000; // Duration of DW motor actuation

bool rpiIsAlive = false;
int graceTime = 5000;
