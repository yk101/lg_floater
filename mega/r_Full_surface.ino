/* The function performs a full surfacing by actuation the pump with a
    bladder setpoint of 650cc.
    The WHILE loop constantly checks the ACCUMULATOR readings to meassure
    bladder inflation.
*/

void FullSurface()
{
  // CHECK IF THE BLADDER IS AT PHYSICAL LIMITS, IF YES EXIT THE FUNCTION
  CalcBladderVol();
  SendMsg("BV", BladdVol);

  if (BladdVol >= BladderUpperLimit)
  {
    return;
  }

  int BladderVolSetPoint = BladderUpperLimit, PumpDirectionBool = HIGH;

  // Reset timers
  PreviousMillis = millis();
  //wdt_enable(WDTO_2S); // enable watchdog timer

  // Feed commands into pump
  digitalWrite(PumpDirectionPin, PumpDirectionBool);
  digitalWrite(ValvePin, HIGH);
  delay(200);
  D2Acmd(100);

  // Verify that the Pump started
  delay(1000);
  PumpRPM = RPMRead();

  int whilecounter = 1;

  // IF THE READ RPM IS BELLOW 1000 -> THE PUMP DIDN'T START,
  // ALLOW 3 TIMES TO RESTART AND THEN ABORT
  while (PumpRPM < 1000)
  {
    wdt_reset(); // reset the watchdog each loop

    D2Acmd(0); // Send STOP signal to pump
    delay(1000);

    PreviousMillis = millis();
    D2Acmd(100);
    delay(1000);

    PumpRPM = RPMRead();
    if (whilecounter >= 3)
    {
      SendMsg("PF", 2);
      return;
    }

    whilecounter = whilecounter + 1;
  }

  //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= WHILE LOOP
  while ((BladderVolSetPoint - 10) > BladdVol)
  {
    wdt_reset(); // reset the watchdog each loop
    delay(50);

    // Calculate bladder volume
    CalcBladderVol();

    if ((BladdVol > BladderUpperLimit) || (BladdVol < BladderLowerLimit))
    {
      D2Acmd(0); // Send STOP signal to pump
      break;
    }
    //-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= END of WHILE LOOP
  }

  wdt_reset();
  //wdt_disable(); // disable watchdog after exit from while() loop

  D2Acmd(0); // Send STOP signal to pump
  delay(200);
  digitalWrite(ValvePin, LOW);
}
