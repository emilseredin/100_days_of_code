def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
keep_going = True
turned_right = 0
while keep_going:
    if at_goal():
        keep_going = False
    elif right_is_clear():
        if turned_right >= 3 and front_is_clear():
            move()
            turned_right = 0
        else:
            turn_right()
            turned_right += 1
            move()
    elif front_is_clear():
        move()
        turned_right = 0
    else:
        turn_left()
        turned_right = 0
