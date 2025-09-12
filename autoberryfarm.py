import minescript as m
import time
import keyboard
import keybinds # From the keybinds files

keyboard.add_hotkey("o", keybinds.kill_script) #1 hot key, 2 script

yaw = 0
pitch = 0
try:
    while not keybinds.stop_flag: # this shi stops, do not touch if not changing it directly.
        yaw += 3  # how much to turn each step, in degrees

    # Wrap yaw into [-180, 180]
        if yaw > 180: # this rotation on positive half of the coordinates.
            yaw -= 360
        elif yaw < -180:
            yaw += 360 # this rotation on negative half of the coordinates.

        m.player_set_orientation(yaw, pitch) #yaw is (z) and (x), pitch is (y)
        m.player_press_use(True) # right click function ON
        time.sleep(0.0005)
finally: # This puppy is just for comfort.
    m.player_press_use(False) # right click function OFF
    m.echo("Script fully stopped.") 