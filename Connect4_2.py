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

grid.showturtle()

marker = turtle.Pen()
marker.up()
marker.right(90)
marker.forward(0.5 * length)
marker.right(90)
marker.forward(3 * width)
marker.right(180)

