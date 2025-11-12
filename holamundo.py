from robot import Robot

left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)

r1 = Robot(left_motor, right_motor, 54, 142)

r1.straight(250)
r1.beep(800, 500)
r1.light_blink(Color.RED, 1000)


