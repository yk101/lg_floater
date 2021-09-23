from collections import deque
# from enum import Flag
from lib.press_sens import Press
from lib.sensor import Sensor
# from lib.press_ctrl import *


class Press_ctrl():
    def __init__(self, avg_samples, precision, epsilon, log):
        self.avg_samples = avg_samples
        self.precision = precision
        self.epsilon = epsilon
        self.log = log
        self.log.info("Pressure controller was initialized successfully")
        self.sensors = {}


    def addSensor(self, header):
        sensor = Press(header,self.avg_samples,self.precision,self.log)
        self.sensors[header]=sensor

    def getSensors(self):
        return self.sensors

    def senseWater(self):
        # TODO: handle failed sensors
        tp1 = self.sensors["TP1"]
        tp2 = self.sensors["TP2"]
        bp1 = self.sensors["BP1"]
        bp2 = self.sensors["BP2"]

        avgTop = ( tp1.getLast() + tp2.getLast() ) / 2 /100
        avgBottom = ( bp1.getLast() + bp2.getLast() ) / 2 / 100

        margin = 0.05

        top_in_range = 10.00 - margin  < avgTop < 10.00 + margin
        bottom_in_range = 10.50  < avgTop

        self.log.debug("10.00 - margin  < avgTop/ < 10.00 + margin")
        self.log.debug(f"10.00 - {margin}  < {avgTop} < 10.00 + {margin}")
        self.log.debug(f"top_in_range {top_in_range}")

        self.log.debug("10.50  < avgBottom")
        self.log.debug(f"10.50  < {avgBottom}")
        self.log.debug(f"bottom_in_range {bottom_in_range}")



        if  top_in_range and bottom_in_range:
            return True

        return False

    def senseAir(self):
        # TODO: handle failed sensors
        tp1 = self.sensors["TP1"]
        tp2 = self.sensors["TP2"]
        avg = tp1.getLast() + tp2.getLast()
        avg/=2

        if 1000 < avg and avg < 1200:
            return True
        return False
