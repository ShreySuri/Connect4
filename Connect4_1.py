import turtle

width = 120
length = 6 * width


grid = turtle.Pen()
grid.hideturtle()
grid.up()
grid.forward(3.5 * width)
grid.left(90)
grid.forward(0.5 * length)
grid.right(180)
grid.down()
for i in range (0,7):
    grid.forward(length)
    grid.right(90)
    grid.forward(width)
    grid.right(90)
    grid.forward(length)
    grid.right(180)


turtle_1 = turtle.Pen()
turtle_1.hideturtle()
turtle_1.up()
turtle_2 = turtle.Pen()
turtle_2.hideturtle()
turtle_2.up()
turtle_3 = turtle.Pen()
turtle_3.hideturtle()
turtle_3.up()
turtle_4 = turtle.Pen()
turtle_4.hideturtle()
turtle_4.up()
turtle_5 = turtle.Pen()
turtle_5.hideturtle()
turtle_5.up()
turtle_6 = turtle.Pen()
turtle_6.hideturtle()
turtle_6.up()
turtle_7 = turtle.Pen()
turtle_7.hideturtle()
turtle_7.up()

turtle_1.right(180)
turtle_1.forward(3 * width)
turtle_1.left(90)
turtle_2.right(180)
turtle_2.forward(2 * width)
turtle_2.left(90)
turtle_3.right(180)
turtle_3.forward(width)
turtle_3.left(90)
turtle_4.right(90)
turtle_5.forward(width)
turtle_5.right(90)
turtle_6.forward(2 * width)
turtle_6.right(90)
turtle_7.forward(3 * width)
turtle_7.right(90)

turtle_1.forward(0.5 * length)
turtle_1.right(180)
turtle_2.forward(0.5 * length)
turtle_2.right(180)
turtle_3.forward(0.5 * length)
turtle_3.right(180)
turtle_4.forward(0.5 * length)
turtle_4.right(180)
turtle_5.forward(0.5 * length)
turtle_5.right(180)
turtle_6.forward(0.5 * length)
turtle_6.right(180)
turtle_7.forward(0.5 * length)
turtle_7.right(180)

turtle_1.pensize(width)
turtle_2.pensize(width)
turtle_3.pensize(width)
turtle_4.pensize(width)
turtle_5.pensize(width)
turtle_6.pensize(width)
turtle_7.pensize(width)

color_1 = input(print("Player 1, choose a color" ))
color_1 = color_1.lower()
color_2 = input(print("Player 2, choose a color" ))
color_2 = color_2.lower()
if color_1 == color_2:
    print("Oops, you picked the same color. ")

player_1 = ["placeholder"]
player_1_diagonal = ["placeholder"]
player_2 = ["placeholder"]
player_2_diagonal = ["placeholder"]
win = False
move_1 = None
move_2 = None
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
counter_7 = 0
turn = 1
append_count_1 = 0
append_count_2 = 0

while win == False:
    while move_1 != 1 or move_1 != 2 or move_1 != 3 or move_1 != 4 or move_1 != 5 or move_1 != 6 or move_1 != 7:
        move_1 = int(input(print("Player 1, which column would you like to place a chip in? Choose an integer from 1 - 7. ")))
    if move_1 == 1:
        turtle_1.pencolor(color_1)
        turtle_1.forward(0.5 * width)
        turtle_1.down
        turtle_1.forward(1)
        turtle_1.up()
        counter_1 = counter_1 + 1
    elif move_1 == 2:
        turtle_2.pencolor(color_1)
        turtle_2.forward(0.5 * width)
        turtle_2.down
        turtle_2.forward(1)
        turtle_2.up()
        counter_2 = counter_2 + 1
    elif move_1 == 3:
        turtle_3.pencolor(color_1)
        turtle_3.forward(0.5 * width)
        turtle_3.down
        turtle_3.forward(1)
        turtle_3.up()
        counter_3 = counter_3 + 1
    elif move_1 == 4:
        turtle_4.pencolor(color_1)
        turtle_4.forward(0.5 * width)
        turtle_4.down
        turtle_4.forward(1)
        turtle_4.up()
        counter_4 = counter_4 + 1
    elif move_1 == 5:
        turtle_5.pencolor(color_1)
        turtle_5.forward(0.5 * width)
        turtle_5.down
        turtle_5.forward(1)
        turtle_5.up()
        counter_5 = counter_5 + 1
    elif move_1 == 6:
        turtle_6.pencolor(color_1)
        turtle_6.forward(0.5 * width)
        turtle_6.down
        turtle_6.forward(1)
        turtle_6.up()
        counter_6 = counter_6 + 1
    elif move_1 == 7:
        turtle_7.pencolor(color_1)
        turtle_7.forward(0.5 * width)
        turtle_7.down
        turtle_7.forward(1)
        turtle_7.up()
        counter_7 = counter_7 + 1
    else:
        print("That isn't an integer from 1 - 7.")

    coordinate = 10 * move_1 + counter
    player_1.append(coordinate)
    append_count_1 = append_count_1 + 1
    if append_count_1 == 1:
        player_1.remove("placeholder")
    elif append_count_1 >= 4:
        player_1.sort()
        for i in range (0, append_count_1 - 3):
            if player_1[i+3] - player_1[i+2] == player_1[i+2] - player_1[i+1] == player_1[i+1] - player_1[i] == 1 :
                win = True
    else:
        win = False
        
    if win == False:
        for i in range(0, append_count_1):
            x = player_1[i] % 10
            y = int((player_1[i] - x)/10)
            coordinate = 10 * x + y
            player_1[i] = coordinate
        if append_count_1 >= 4:
            player_1.sort()
            for i in range (0, append_count_1 - 3):
                if player_1[i+3] - player_1[i+2] == player_1[i+2] - player_1[i+1] == player_1[i+1] - player_1[i] == 1 :
                    win = True
        else:
            win = False

    for i in range(0, append_count_1):
        x = player_1[i] % 10
        y = int((player_1[i] - x)/10)
        coordinate = 10 * x + y
        player_1[i] = coordinate
    
