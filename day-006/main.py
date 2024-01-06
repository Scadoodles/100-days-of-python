def turn_right():
    turn_left()
    turn_left()
    turn_left()

def seek_and_move():
    if wall_on_right() and not wall_in_front():
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif not wall_on_right():
        turn_right()
        move()
    else:
        move()
    
while not at_goal():
    seek_and_move()
