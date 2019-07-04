from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from threading import Thread

class DeflectObstacle():
    def __init__(self, motorDirectionLeft, motorDirectionRight,sensorColorLeft,sensorColorRight):
        self.motorDirectionLeft = motorDirectionLeft
        self.motorDirectionRight = motorDirectionRight
        self.sensorColorLeft = sensorColorLeft
        self.sensorColorRight = sensorColorRight
    
    def deflect(self):
        motorMovementForward = DriveBase(self.motorDirectionLeft,self.motorDirectionRight,30,30)
        self.motorDirectionRight.drive_time(50,0,2000)
        motorMovementForward.drive_time(50,0,3000)
        self.motorDirectionRight.drive_time(50,0,2000)
        motorMovementForward.drive_time(50,0,5000)
        self.motorDirectionRight.drive_time(50,0,1500)
        

        while(self.sensorColorRight.reflection() > 30):
            motorMovementForward.drive()
        while(self.sensorColorLeft.reflection() > 30):
            self.motorDirectionRight.drive()