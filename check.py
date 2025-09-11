import minescript as m

from minescript_plus import World

import time

Dificulty = World.get_difficulty()
Time = World.get_game_time()

m.echo(f"World Data: /n Dificulty:{Dificulty}, /n, In game time:{Time}")

time.sleep(3)