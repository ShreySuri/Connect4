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

color_1 = input(print("Player 1, choose a color" )
color_1 = color_1.lower()
color_2 = input(print("Player 2, choose a color" )
color_2 = color_2.lower()
if color_1 == color_2:
    print("Oops, you picked the same color. ")

player_1 = None
player_2 = None
win = False

while win == False:
    move_1 = int(input(print("Player 1, which column would you like to place a chip in? ")))
    if move_1 == 1:
        turtle_1.pencolor(color_1)
        turtle_1.down
        



