from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


from robot import Robot

left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
#ultrasonido = UltrasonicSensor(Port.C)
color = ColorSensor(Port.A)


r2 = Robot(left_motor, right_motor, 56, 143)
#r2.guardar_sensor('ultra', ultrasonido)
r2.guardar_sensor('color', color)

#suponemos que el robot comienza en la esq 1. mirando al sur
#
#    3     4        NORTE             ROJO       AMARILLO
#              OESTE     ESTE
#    1     2         SUR              AZUL       VERDE
#ROJO ir a esquina 1
#VERDE  ir a esquina 3
#AZUL ir a esquina 4
#AMARILLO   ir a esquina 2
freq = {
    Color.RED: 250,
    Color.BLUE: 1000,
    Color.WHITE: 500,
    Color.GREEN: 750,
}

# El robot comienza en la esquina 1 mirando al norte

movimientos = {
    (Color.RED, 2, 'Norte'): [ [('turn',(90,)), ['straight', (850,)] ], 1, "Oeste"],
    (Color.RED, 2, 'Sur'): [ [('turn',(-90,)), ['straight', (850,)] ], 1, "Oeste"],
    (Color.RED, 2, 'Este'):  [ [('turn',(180,)), ['straight', (850,)] ], 1, 'Oeste'],
    (Color.RED, 2, 'Oeste'): [ [['straight', (850,)] ], 1, 'Oeste'],
    (Color.GREEN, 1, 'Oeste'): [ [('turn',(-90,)), ['straight', (850,)] ], 3, "Norte"],
    (Color.GREEN, 1, 'Este'): [ [('turn',(90,)), ['straight', (850,)] ], 3, "Norte"],
    (Color.GREEN, 1, 'Sur'):  [ [('turn',(180,)), ['straight', (850,)] ], 3, 'Norte'],
    (Color.GREEN, 1, 'Norte'): [ [['straight', (850,)] ], 3, 'Norte'],
    (Color.BLUE, 'Norte'): [ [('turn',(90,)), ['straight', (850,)] ], 1, "Oeste"],
    (Color.BLUE, 2, 'Sur'): [ [('turn',(-90,)), ['straight', (850,)] ], 1, "Oeste"],
    (Color.BLUE, 2, 'Este'):  [ [('turn',(180,)), ['straight', (850,)] ], 1, 'Oeste'],
    (Color.BLUE, 2, 'Oeste'): [ [['straight', (850,)] ], 1, 'Oeste'],
    (Color.YELLOW, 1, 'Oeste'): [ [('turn',(-90,)), ['straight', (850,)] ], 3, "Norte"],
    (Color.YELLOW, 1, 'Este'): [ [('turn',(90,)), ['straight', (850,)] ], 3, "Norte"],
    (Color.YELLOW, 1, 'Sur'):  [ [('turn',(180,)), ['straight', (850,)] ], 3, 'Norte'],
    (Color.YELLOW, 1, 'Norte'): [ [['straight', (850,)] ], 3, 'Norte'],

}

esquina = 2
orientacion = 'Norte'

while True:
    sensor = r2.sensor('color').color()
    key = (sensor, esquina, orientacion)
    print(key)

    historia, esquina, orientacion = movimientos.get(key, [[], esquina, orientacion])


    print(sensor)
    r2.beep(freq[sensor], 1000)
    r2.hacer_historia(historia)





