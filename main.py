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

brick.sound.beep()

brick.display.clear()

# Engine declaration
motorDirectionLeft = Motor(Port.A)
#motorRideUp = Motor(Port.B)
#motorGoDown = Motor(Port.C)
motorDirectionRight = Motor(Port.D)

# Sensor declaration
sensorColorLeft = ColorSensor(Port.S1)
sensorUltrassonicLeft = UltrasonicSensor(Port.S2)
#sensorUltrassonicRight = UltrasonicSensor(Port.S3)
sensorColorRight = ColorSensor(Port.S4)

#Movements
motorMovementForward = DriveBase(motorDirectionLeft,motorDirectionRight,30,30)
motorMovementRigth = DriveBase(motorDirectionLeft,motorDirectionRight,-20,32)
motorMovementLeft = DriveBase(motorDirectionLeft,motorDirectionRight,20,-32)

# Function follow track
def followTrack():

    if(sensorColorLeft.reflection() < 30 and sensorColorRight.reflection() > 30):
        brick.display.text("Right", (60, 50))
        motorMovementRigth.drive(0,128)
        brick.display.clear()
        wait(1)
        
    elif (sensorColorLeft.reflection() > 30 and sensorColorRight.reflection() < 30):
        brick.display.text("Left", (60, 50))
        motorMovementLeft.drive(0,-128)
        brick.display.clear()
        wait(1)

    elif(sensorColorLeft.reflection() > 30 and sensorColorLeft.reflection() > 30):
        brick.display.text("White", (60, 50))
        motorMovementForward.drive(60,0)
        brick.display.clear()
    
    else:
        brick.display.text("Black", (60, 50))
        motorMovementForward.drive(20,0)
        brick.display.clear()
# Function deflect obstacle
#def deflectObstacle():

# Function rescue
#def rescue():

# Function detects gray
#def detectsGray():

def main():
    while True:
        followTrack()
main()
