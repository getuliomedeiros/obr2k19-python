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

from followLine import FollowLine
from deflectObstacle import DeflectObstacle

# Follow line
follow_line = FollowLine(Motor(Port.A),Motor(Port.B),ColorSensor(Port.S1),ColorSensor(Port.S4),UltrasonicSensor(Port.S2))
follow_line.follow()

# Deflect obstacle
deflect_obstacle = DeflectObstacle(Motor(Port.A),Motor(Port.B),ColorSensor(Port.S1),ColorSensor(Port.S4))
deflect_obstacle.deflect()
