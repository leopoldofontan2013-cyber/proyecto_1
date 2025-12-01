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

freq = {
    Color.RED: 250,
    Color.BLUE: 1000,
    Color.WHITE: 500,
    Color.GREEN: 750,
}

# El robot comienza en la esquina 1 mirando al norte

movimientos = {
    Color.RED: [('turn',(90,)), ['straight', (850,)] ],
    Color.WHITE: [('turn',(90,)), ['straight', (850,)] ],
    Color.GREEN: [('turn',(90,)), ['straight', (850,)] ],
    Color.BLUE: [('turn',(90,)), ['straight', (850,)] ],
}

while True:
    sensor = r2.sensor('color').color()
    print(sensor)
    r2.beep(freq[sensor], 1000)
    r2.hacer_historia(movimientos.get(sensor, []))    
    









