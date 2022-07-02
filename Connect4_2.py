import turtle





width = 120
length = 6 * width


colors = ["red", "pink", "orange","yellow","green","teal","blue","indigo","purple", "tan"]
color_count = 10

color_1_checker = False

while color_1_checker == False:
    print("")
    color_1 = input(print("Player 1, please choose a color. If you would like a list of colors, type 'list'."))
    color_1 = color_1.lower()
    if color_1 == "list":
        print("")
        for i in range (0, color_count):
            print(colors[i])
    else:
        for i in range (0, color_count):
            if colors[i] == color_1:
                color_1_checker = True
            else:
                color_1_checker = color_1_checker

color_2_checker = False

while color_2_checker == False:
    print("")
    color_2 = input(print("Player 2, please choose a color. If you would like a list of colors, type 'list'."))
    color_2 = color_2.lower()
    if color_2 == "list":
        print("")
        for i in range (0, color_count):
            print(colors[i])
    elif color_2 != color_1:
        for i in range (0, color_count):
            if colors[i] == color_1:
                color_2_checker = True
            else:
                color_2_checker = color_2_checker
    else:
        print("")
        print("This color has been chosen by Player 1. Please choose a different color.")


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


marker = turtle.Pen()
marker.up()
marker.right(90)
marker.forward(0.5 * length)
marker.right(90)
marker.forward(3 * width)
marker.right(180)

win = False

while win = False:
    

