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

#brick.sound.beep()
brick.display.clear()

# Engine declaration --------------------------------------------------------------------
motorDirectionLeft = Motor(Port.A)
#motorRideUp = Motor(Port.B)
#motorGoDown = Motor(Port.C)
motorDirectionRight = Motor(Port.D)

# Sensor declaration --------------------------------------------------------------------
sensorColorLeft = ColorSensor(Port.S1)
sensorUltrassonicFront = UltrasonicSensor(Port.S2)
#sensorUltrassonicSide = UltrasonicSensor(Port.S3)
sensorColorRight = ColorSensor(Port.S4)

#Movements --------------------------------------------------------------------------------
motorMovementForward = DriveBase(motorDirectionLeft,motorDirectionRight,30,30)
motorMovementTurn = DriveBase(motorDirectionLeft,motorDirectionRight,20,-32)

# Function detect green -------------------------------------------------------------------
def detectGreenRight():

    contGreen = 0
    motorMovementTurn.drive(-20,0)
    wait(100)
    motorMovementForward.drive(0,0)
    wait(10)

    print("R1")
    for i in range(500):
        if sensorColorRight.color() == 2:
            contGreen += 1
        else:
            contGreen += 0

    print("R2")
    for i in range(500):
        if sensorColorRight.color() == 2:
            contGreen += 1
        else:
            contGreen += 0

    if contGreen >= 999:
        print("Green")
        motorMovementForward.drive(100,0)
        brick.display.text("Right Green", (60, 50))
        wait(400)
        motorMovementTurn.drive(0,-256)
        wait(256)
        motorMovementTurn.drive(0,-128)
        while sensorColorLeft.reflection() > 30:
            wait(10) 
        brick.display.clear()
    contGreen = 0

def detectGreenLeft():

    contGreen = 0
    motorMovementTurn.drive(20,0)
    wait(100)
    motorMovementForward.drive(0,0)
    wait(10)

    print("L1")
    for i in range(500):
        if sensorColorLeft.color() == 2:
            contGreen += 1
        else:
            contGreen += 0

    print("L2")
    for i in range(500):
        if sensorColorLeft.color() == 2:
            contGreen += 1
        else:
            contGreen += 0

    if contGreen >= 999:
        print("Green")
        motorMovementForward.drive(100,0)
        wait(400)
        brick.display.text("Left Green", (60, 50))
        motorMovementTurn.drive(0,256)
        wait(256)
        motorMovementTurn.drive(0,128)
        while sensorColorRight.reflection() > 30:
            wait(10)
        brick.display.clear()
    contGreen = 0

def doubleGreen():
    contGreen = 0
    motorMovementTurn.drive(20,0)
    wait(100)
    motorMovementForward.drive(0,0)
    wait(10)

    print("LR")
    for i in range(500):
        if sensorColorLeft.color() == 2 and sensorColorRight.color() == 2:
            contGreen += 1
        else:
            contGreen += 0

    print("LR")
    for i in range(500):
        if sensorColorLeft.color() == 2 and sensorColorRight.color() == 2:
            contGreen += 1
        else:
            contGreen += 0
    
    if contGreen >= 999:
        print("Green")
        brick.display.text("Left Green", (60, 50))
        motorMovementForward.drive(-100,0)
        wait(512)
        motorMovementTurn.drive(0,128)
        wait(1256)
        motorMovementTurn.drive(0,128)
        while sensorColorRight.reflection() > 30:
            wait(10)
        brick.display.clear()
    contGreen = 0

# Function follow track -------------------------------------------------------------------
def followTrack():

    if sensorColorLeft.reflection() < 30 and sensorColorRight.reflection() > 30:
        if sensorColorLeft.color() == 2:
            contGreen = 0
            motorMovementForward.drive(0,0)
            wait(1)
            for i in range(11):
                if sensorColorLeft.color() == 2:
                    contGreen += 1
                else:
                    contGreen += 0
            if contGreen >= 9:
                detectGreenLeft()
            else:
                motorMovementTurn.drive(0,-128)
                while sensorColorRight.reflection() > 30:
                    wait(10)
                brick.display.clear()
            contGreen = 0        
        else:
            brick.display.text("Right", (60, 50))
            motorMovementTurn.drive(0,128)
            while sensorColorLeft.reflection() < 30:
                wait(10)
            brick.display.clear() 

    elif sensorColorLeft.reflection() > 30 and sensorColorRight.reflection() < 30:
        if sensorColorRight.color() == 2:
            contGreen = 0
            motorMovementForward.drive(0,0)
            wait(1)
            for i in range(11):
                if sensorColorRight.color() == 2:
                    contGreen += 1
                else:
                    contGreen += 0
            if contGreen >= 9:
                detectGreenRight()
            else:
                motorMovementTurn.drive(0,128)
                while sensorColorLeft.reflection() > 30:
                    wait(10)
                brick.display.clear() 
            contGreen = 0
        else:
            brick.display.text("Left", (60, 50))
            motorMovementTurn.drive(0,-128)
            while sensorColorRight.reflection() < 30:
                wait(10)
            brick.display.clear() 

    elif sensorColorLeft.reflection() > 30 and sensorColorLeft.reflection() > 30:
        brick.display.text("White", (60, 50))
        motorMovementForward.drive(60,0)
        brick.display.clear()

    else:
        if sensorColorLeft.color() == 2 and sensorColorRight.color() == 2:
            contGreen = 0
            motorMovementForward.drive(0,0)
            for i in range(11):
                if sensorColorLeft.color() == 2 and sensorColorRight.color() == 2:
                    contGreen += 1
                else:
                    contGreen += 0
            if contGreen >= 9:
                doubleGreen()
            else:
                motorMovementForward.drive(20,0)

        else:
            brick.display.text("Black", (60, 50))
            motorMovementForward.drive(20,0)
            brick.display.clear()
        
# Function deflect obstacle ---------------------------------------------------------------
def deflectObstacle():
    motorMovementForward.drive(-100,0)
    wait(512)

# Function rescue -------------------------------------------------------------------------
#def rescue():

# Function detects gray -------------------------------------------------------------------
#def detectsGray():

# Function main ---------------------------------------------------------------------------
def main():
    while True:
        if sensorUltrassonicFront.distance() < 100:
            deflectObstacle()
        else:
            followTrack()

main()
