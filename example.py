import minescript
import numpy as np

# Get and convert player position
x, y, z = minescript.player_position()
x, y, z = int(x), int(y), int(z)

#degrees = 0

minescript.echo(f"You are here daddy: X={x}, Y={y}, Z={z}")

#while True:
    #x = np.cos(degrees)
    #z = np.sin(degrees)
    #minescript.player.look_at(int(x), int(y+1), int(z))
    #degrees += np.pi/8


