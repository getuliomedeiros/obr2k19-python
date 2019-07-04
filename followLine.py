from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from threading import Thread

class FollowLine():
    def __init__(self, motorDirectionLeft, motorDirectionRight,sensorColorLeft,sensorColorRight, sensorUltrassonicLeft):
        self.motorDirectionLeft = motorDirectionLeft
        self.motorDirectionRight = motorDirectionRight
        self.sensorColorLeft = sensorColorLeft
        self.sensorColorRight = sensorColorRight
        self.sensorUltrassonicLeft = sensorUltrassonicLeft
    
    def follow(self):
        motorMovementRight = DriveBase(self.motorDirectionLeft,self.motorDirectionRight,20,-32)
        motorMovementLeft = DriveBase(self.motorDirectionLeft,self.motorDirectionRight,-32,20)
        motorMovementForward = DriveBase(self.motorDirectionLeft,self.motorDirectionRight,30,30)
        motorMovementForwardReduced = DriveBase(self.motorDirectionLeft,self.motorDirectionRight,15,15)
        
        while(self.sensorUltrassonicLeft.distance() < 10000):
            if (self.sensorColorLeft.reflection() > 30):
                if(self.sensorColorRight.reflection() > 30):
                    motorMovementForward.drive()
                else:
                    motorMovementRight.drive()
            else:
                if(self.sensorColorRight.reflection() > 30):
                    motorMovementLeft.drive()
                else:
                    motorMovementForwardReduced.drive()