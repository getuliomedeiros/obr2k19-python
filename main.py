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

# Engine declaration ----------------------------------------------------------------------
motorDirectionLeft = Motor(Port.A)
#motorRideUp = Motor(Port.B)
#motorGoDown = Motor(Port.C)
motorDirectionRight = Motor(Port.D)

# Sensor declaration ----------------------------------------------------------------------
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
    motorMovementTurn.drive(-64,0)
    wait(100)
    motorMovementForward.drive(0,0)
    wait(100)

    print("Loop from confirmed Right Sensor")
    for i in range(1000):
        if sensorColorRight.color() == 2:
            contGreen += 1

    if contGreen >= 999:
        brick.sound.beep()
        print("Green")
        motorMovementForward.drive(100,0)
        brick.display.text("Right Green", (60, 50))
        wait(400)
        motorMovementTurn.drive(0,-256)
        wait(256)
        motorMovementTurn.drive(0,-128)
        while sensorColorLeft.reflection() > 30:
            wait(10) 
        motorMovementTurn.drive(0,256)
        wait(430)
        brick.display.clear()
    contGreen = 0

def detectGreenLeft():

    contGreen = 0
    motorMovementTurn.drive(-64,0)
    wait(100)
    motorMovementForward.drive(0,0)
    wait(100)

    print("Loop from confirmed Left Sensor")
    for i in range(1000):
        if sensorColorLeft.color() == 2:
            contGreen += 1

    if contGreen >= 999:
        brick.sound.beep()
        print("Green")
        motorMovementForward.drive(100,0)
        wait(400)
        brick.display.text("Left Green", (60, 50))
        motorMovementTurn.drive(0,256)
        wait(256)
        motorMovementTurn.drive(0,128)
        while sensorColorRight.reflection() > 30:
            wait(10)
        motorMovementTurn.drive(0,-256)
        wait(430)
        brick.display.clear()
    contGreen = 0

def doubleGreen():
    contGreen = 0
    motorMovementTurn.drive(-64,0)
    wait(100)
    motorMovementForward.drive(0,0)
    wait(100)

    print("Loop from confirmed Double Sensor")
    for i in range(1000):
        if sensorColorLeft.color() == 2 and sensorColorRight.color() == 2:
            contGreen += 1

    if contGreen >= 999:
        brick.sound.beep()
        print("Green")
        brick.display.text("Left Green", (60, 50))
        motorMovementForward.drive(-100,0)
        wait(512)
        motorMovementTurn.drive(0,128)
        wait(1256)
        motorMovementTurn.drive(0,128)
        while sensorColorRight.reflection() > 30:
            wait(10)
        motorMovementTurn.drive(0,-256)
        wait(430)
        brick.display.clear()
    contGreen = 0

# Function follow track -------------------------------------------------------------------
def followTrack():

    if sensorColorLeft.reflection() < 50 and sensorColorRight.reflection() > 50: # side left
        if sensorColorLeft.color() == 2: # detect green left
            contGreen = 0
            motorMovementForward.drive(0,0)
            wait(1000)
            for i in range(11): # for from detection green
                if sensorColorLeft.color() == 2:
                    contGreen += 1
            if contGreen >= 9: # confirmation green
                detectGreenLeft()
            else: # green not confirmed
                motorMovementTurn.drive(0,128)
                while sensorColorRight.reflection() > 30:
                    wait(10)
                motorMovementTurn.drive(0,-128)
                wait(100)
                brick.display.clear()
            contGreen = 0        
        else: # side right
            motorMovementTurn.drive(0,128)
            while sensorColorRight.reflection() > 30:
                wait(10)
            motorMovementTurn.drive(0,-256)
            wait(430)
            motorMovementTurn.drive(0,0)
            wait(256)
            brick.display.clear()

    elif sensorColorLeft.reflection() > 50 and sensorColorRight.reflection() < 50: # side right
        if sensorColorRight.color() == 2: # detect green right
            contGreen = 0
            motorMovementForward.drive(0,0)
            wait(1000)
            for i in range(11): # for from detection green
                if sensorColorRight.color() == 2: # confirmation green
                    contGreen += 1
            if contGreen >= 9:
                detectGreenRight()
            else: # green not confirmed
                motorMovementTurn.drive(0,-128)
                while sensorColorLeft.reflection() > 30:
                    wait(10)
                motorMovementTurn.drive(0,128)
                wait(100)
                brick.display.clear() 
            contGreen = 0
        else: # side left
            motorMovementTurn.drive(0,-128)
            while sensorColorLeft.reflection() > 30:
                wait(10)
            motorMovementTurn.drive(0,256)
            wait(430)
            motorMovementTurn.drive(0,0)
            wait(256)
            brick.display.clear() 

    elif sensorColorLeft.reflection() > 50 and sensorColorLeft.reflection() > 50: # white
        brick.display.text("White", (60, 50))
        motorMovementForward.drive(100,0)
        brick.display.clear()

    else: # black
        if sensorColorLeft.color() == 2 and sensorColorRight.color() == 2:
            contGreen = 0
            motorMovementForward.drive(-100,0)
            wait(500)
            motorMovementForward.drive(0,0)
            wait(1000)
            for i in range(11):
                if sensorColorLeft.color() == 2 and sensorColorRight.color() == 2:
                    contGreen += 1
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
    brick.display.text("Obstacle", (60, 50))
    motorMovementForward.drive(0,0) # stop
    wait(100) # delay stop
    motorMovementForward.drive(-50,0) # back
    wait(1000) # delay back
    motorMovementForward.drive(0,0) # stop
    wait(100) # delay stop
    motorMovementTurn.drive(0,-256) # side right 
    wait(1000) # delay side rigth
    motorMovementForward.drive(0,0) # stop
    wait(100) # delay stop
    motorMovementForward.drive(70,0) # front
    wait(3000) # delay front
    motorMovementForward.drive(0,0)
    wait(100) # delay stop
    motorMovementTurn.drive(0,256) # side left
    wait(1000) # delay side left
    motorMovementForward.drive(70,0) # front
    wait(4000) # delay front
    motorMovementTurn.drive(0,256) # side left
    wait(550) # delay side left
    motorMovementForward.drive(50,0) # front search line
    wait(1000)
    motorMovementForward.drive(50,0) # front search line
    while sensorColorRight.reflection() > 30:
        wait(10)
    motorMovementTurn.drive(0,-256) # side right
    while sensorColorLeft.reflection() > 30:
        wait(10)

# Function rescue init --------------------------------------------------------------------
#def rescueInit():

# Function rescue -------------------------------------------------------------------------
#def rescue():

# Function main ---------------------------------------------------------------------------
def main():
    while True:
        if sensorUltrassonicFront.distance() < 100:
            deflectObstacle()
        else:
            followTrack()

main()
