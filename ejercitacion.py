from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


from robot import Robot

left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
#ultrasonido = UltrasonicSensor(Port.C)
color = ColorSensor(Port.A)


r2 = Robot(left_motor, right_motor, 56, 143)
#r2.guardar_sensor('ultra', ultrasonido)
r2.guardar_sensor('color', color)

if r2.sensor('color').color() == Color.RED:
    r2.beep(250, 1000)
    r2.straight(900)

if r2.sensor('color').color() == Color.GREEN:
    r2.beep(500, 1000)
    r2.turn(90)
    r2.straight(850)
    
if r2.sensor('color').color() == Color.BLUE:
    r2.beep(1000, 1000)
    r2.turn(90)
    r2.straight(900)

if r2.sensor('color').color() == Color.YELLOW:
    r2.beep(750, 1000)
    r2.turn(90)
    r2.straight(900)









