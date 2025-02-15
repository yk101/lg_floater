import datetime
import os
import sys
from time import sleep, time
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path + os.sep + "cfg")
import configuration as cfg

class PID:
    def __init__(self):
        last_cmd_was_sent_at = None
        self.doInterpolation = False

    def get_next_move(self, curr_press):
        setpoint_err = cfg.task["setpoint"] - curr_press
        cmd = "U:" if setpoint_err < 0 else "D:"

        if abs(setpoint_err) > cfg.task["fullduty_min_distance"]: #fullduty mode
            last_cmd_was_sent_at = datetime.datetime.Now()
            return cmd + cfg.task["fullduty_exec_time"]
        else: #partial mode
            coefficient = cfg.task["setpoint"] - abs(setpoint_err)/cfg.task["setpoint"]
            partial_duty_exec_time = coefficient * cfg.task["fullduty_exec_time"]
            partial_duty_sleep_time = self.interp(setpoint_err)
            if partial_duty_sleep_time < (datetime.datetime.Now() - self.last_cmd_was_sent_at):
                pass

    # absolute value and limit between 40% to 100%
    def normal_pumpVoltage(self, current_err):
        voltage = abs(current_err)
        if voltage >= 100:
            voltage = 100
        if voltage <= 40:
            voltage = 40
            # voltage = 0

        # print("voltage", voltage)
        return voltage

    def getDirection(self,curr_err):
        # up (D:1)
        # down (D:2)
        return 1 if curr_err > 0 else 2
        
    def interp_timeOn(self, current_err):
        current_err = abs(current_err)
        if current_err > 100:
            current_err = 100
        x1 = 0 # no error - spot on target!
        x2 = 100 # max error
        y1 = 0.5 # min timeOn is 0.5 sec
        y2 = 5 # max timeOn is 5 secs

        m = (y2-y1)/(x2-x1)

        # print("m",m)

        timeOn = 0.5 + m * current_err
        # print("timeOn",timeOn)
        return timeOn

    def interp_dutyCycle(self, current_err):
        current_err = abs(current_err)
        if current_err > 100:
            current_err = 100

        x1 = 0 # no error
        x2 = 100 # max error
        y1 = 0 # min utility 0% (min dc)
        y2 = 1 # max utility 100% (max dc)

        m = (y2-y1)/(x2-x1)
        # print("m",m)

        dc = 0.0 + m * current_err
        # print("duty cycle", dc)
        return dc

    def calc_timeOff(self, timeOn, dc):
        # dc = timeOn/(timeOn+timeOff)
        # dc * (timeOn+timeOff) = timeOn
        # dc * timeOn + dc * timeOff = timeOn
        # timeOff * dc = timeOn - dc * timeOn
        # timeOff = timeOn / dc - timeOn
        # timeOff = (timeOn * (1-dc) )/dc


        # dc = timeOn/(timeOn+timeOff)
        # dc * (timeOn+timeOff) = timeOn
        # timeOn + timeOff = timeOn / dc
        timeOff = timeOn / dc - timeOn
        # print("timeOff",timeOff)
        return timeOff


if __name__ == "__main__":
    pid = PID()
    # pid.interp_pumpVoltage(100)
    # pid.interp_pumpVoltage(90)
    # pid.interp_pumpVoltage(80)
    # pid.interp_pumpVoltage(70)
    # pid.interp_pumpVoltage(60)
    # pid.interp_pumpVoltage(50)
    # pid.interp_pumpVoltage(40)
    # pid.interp_pumpVoltage(30)
    # pid.interp_pumpVoltage(20)
    # pid.interp_pumpVoltage(10)
    # pid.interp_pumpVoltage(5)

    for err in range(100,0,-10):
        print("error",err)
        timeOn = pid.interp_timeOn(err)
        dc = pid.interp_dutyCycle(err)
        timeOff = pid.calc_timeOff(timeOn,dc)
        print("timeOff",timeOff)
    # pid.interp_dutyCycle(100)
    # pid.interp_dutyCycle(90)
    # pid.interp_dutyCycle(80)
    # pid.interp_dutyCycle(70)
    # pid.interp_dutyCycle(60)
    # pid.interp_dutyCycle(50)
    # pid.interp_dutyCycle(40)
    # pid.interp_dutyCycle(30)
    # pid.interp_dutyCycle(20)
    # pid.interp_dutyCycle(10)
    # pid.interp_dutyCycle(5)

    



