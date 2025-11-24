from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from robot import Robot
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F, Direction.CLOCKWISE)
ultrasonido = UltrasonicSensor(Port.C)
color = ColorSensor(Port.A)


r2 = Robot(left_motor, right_motor, 56, 142)
r2.guardar_sensor('ultra', ultrasonido)
r2.guardar_sensor('color', color)

sonidos = {
    Color.RED: 800,
    Color.BLUE: 1000,
    Color.WHITE: 1200,
    Color.BLACK: 1400,
}
while True:
    c = r2.sensor('color').color()
    print(c)
    r2.beep(sonidos[c],1000)
    wait(1000)
#r2.straight(250)
#r2.turn(90)
#r2.straight(200)
#r2.turn(-90)
#r2.beep(800, 500)
#r2.deshacer_historia()


