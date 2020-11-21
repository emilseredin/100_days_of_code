def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
# move forward if possible
# if not, turn left, move forward
# then turn right, move forward
# afterwards turn right again and move forward
# then turn left
while not at_goal():
    jump()    
