import minescript as m
import math
import time

degrees = 0
 
m.player_set_orientation(0, 0)

while True:
    m.player_press_use(True)
    z = math.sin(degrees)
    degrees += math.radians(1)
    time.sleep(0.1)
    m.player_set_orientation(z * 180, 0)
#   m.echo(i)