void RunMotor()
{
//  digitalWrite(DirectionPin, HIGH);
//  analogWrite(MotorPin, 255);
//  delay(MotorTime);
//  analogWrite(MotorPin, 0);
//  delay(500);
//
//  digitalWrite(DirectionPin, LOW);
//  analogWrite(MotorPin, 255);
//  delay(MotorTime);
//  analogWrite(MotorPin, 0);
  
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(2500);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);  
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(2500);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW); 
}
