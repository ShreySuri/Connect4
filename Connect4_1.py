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
turtle_1.forward
