from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Robot:
    def __init__(self, left_motor, right_motor,wheel_diameter, axle_track):
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
        self.hub = PrimeHub()
        self.drive_base.use_gyro(True)
        self.historia = []
        self.sensores = dict()

    def guardar_sensor(self, nombre, sensor):
        self.sensores[nombre] = sensor

    def sensor(self, nombre):
        return self.sensores.get(nombre)

    #Movimiento
    def straight(self, distance, guardar = True):
        self.drive_base.straight(distance)
        if guardar:
            self.historia.append(["straight", [distance]])
            print(self.historia)

    def turn(self, angle, guardar = True):
        self.drive_base.turn(angle)
        if guardar:
            self.historia.append(["turn", [angle]])
            print(self.historia)

    def deshacer(self, inst):
        if inst[0] == "straight":
            distance = inst[1][0]
            self.straight(-distance, guardar=False)
        elif inst[0] == "turn":
            angle = inst[1][0]
            self.turn(-angle, guardar = False)

    def deshacer_historia(self):
        for inst in reversed(self.historia):
            self.deshacer(inst)
    
    def hacer(self, inst):
        if inst[0] == 'straight':
            distance =  inst[1][0]
            self.straight(distance, guadar=False)
        elif inst[0] == "turn":
            angle = inst[1][0]
            self.turn(-angle, guardar = False)

    def hacer_historia(self, historia):
        for inst in historia:
            self.deshacer(inst)


    #Sonido
    def beep(self, freq, duration):
        self.hub.speaker.beep(freq, duration)

    def play_notes(self, notes):
        self.hub.speaker.play_notes(notes)

    #Luces
    def light_off(self):
        self.hub.light.off()

    def light_blink(self, color, durations):
        self.hub.light.blink(color, durations)

    def light_animate(self, colors, interval):
        self.hub.light.animate(colors, interval)
        

        

