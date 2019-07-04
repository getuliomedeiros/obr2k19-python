#!/usr/bin/env pybricks-micropython

# Program developer
# Álvaro Getúlio Lima Medeiros
# Informática - 201513530194
# IFPB - Campus Picuí

# Library import
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from threading import Thread

# Engine declaration
motorDirectionLeft = Motor(Port.A)
motorRideUp = Motor(Port.B)
motorGoDown = Motor(Port.C)
motorDirectionRight = Motor(Port.D)

# Sensor declaration
sensorColorLeft = ColorSensor(Port.S1)
sensorUltrassonicLeft = UltrasonicSensor(Port.S2)
sensorUltrassonicRight = UltrasonicSensor(Port.S3)
sensorColorRight = ColorSensor(Port.S4)

# Code body
#followTrack = Thread(target=followTrack)
#followTrack.start()
#deflectObstacle = Thread(target=deflectObstacle)
#deflectObstacle.start()

# Function follow track
def followTrack(sc1, sc2, m1, m2):
    motorMovementRight = DriveBase(m1,m2,20,-32)
    motorMovementLeft = DriveBase(m1,m2,-32,20)
    motorMovementForward = DriveBase(m1,m2,30,30)
    motorMovementForwardReduced = DriveBase(m1,m2,15,15)
    if (sc1.value() > 30):
        if(sc2.value() > 30):
            motorMovementForward.drive()
        else:
            motorMovementRight.drive()
    else:
        if(sc2.value() > 30):
            motorMovementLeft.drive()
        else:
            motorMovementForwardReduced.drive()

# Function deflect obstacle
def deflectObstacle(su1, m1, m2,sc1, sc2):
    motorMovementRight = DriveBase(m1,m2,20,-32)
    motorMovementLeft = DriveBase(m1,m2,-32,20)
    motorMovementForward = DriveBase(m1,m2,30,30)
    if(su1.distance() < 10):
        motorDirectionRight.drive_time(50,0,2000)
        motorMovementForward.drive_time(50,0,3000)
        motorDirectionRight.drive_time(50,0,2000)
        motorMovementForward.drive_time(50,0,5000)
        motorDirectionRight.drive_time(50,0,1500)
        while(sc2.value() > 30):
            motorMovementForward.drive()
        while(sc1.value() > 30):
            motorDirectionRight.drive()

# Function rescue
#def rescue():

# Function detects gray
#def detectsGray():