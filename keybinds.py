stop_flag = False #Global termination flag

def kill_script(): # killing the script
    import minescript as m
    global stop_flag # global kill switch
    m.echo(f"stopping...")
    stop_flag = True

