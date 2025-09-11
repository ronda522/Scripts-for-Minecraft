import minescript

# Get and convert player position
x, y, z = minescript.player_position()
x, y, z = int(x), int(y), int(z)

minescript.echo(f"You are here daddy: X={x}, Y={y}, Z={z}")


