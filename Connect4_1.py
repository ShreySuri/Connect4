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
