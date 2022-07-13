import turtle

def add_to_list(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    if n == 1:
        win_list_1[a] = win_list[a] + 1
        win_list_1[b] = win_list[b] + 1
        win_list_1[c] = win_list[c] + 1
        win_list_1[d] = win_list[d] + 1
        win_list_1[e] = win_list[e] + 1
        win_list_1[f] = win_list[f] + 1
        win_list_1[g] = win_list[g] + 1
        win_list_1[h] = win_list[h] + 1
        win_list_1[i] = win_list[i] + 1
        win_list_1[j] = win_list[j] + 1
        win_list_1[k] = win_list[k] + 1
        win_list_1[l] = win_list[l] + 1
        win_list_1[m] = win_list[m] + 1
    elif n == 2:
        win_list_2[a] = win_list[a] + 1
        win_list_2[b] = win_list[b] + 1
        win_list_2[c] = win_list[c] + 1
        win_list_2[d] = win_list[d] + 1
        win_list_2[e] = win_list[e] + 1
        win_list_2[f] = win_list[f] + 1
        win_list_2[g] = win_list[g] + 1
        win_list_2[h] = win_list[h] + 1
        win_list_2[i] = win_list[i] + 1
        win_list_2[j] = win_list[j] + 1
        win_list_2[k] = win_list[k] + 1
        win_list_2[l] = win_list[l] + 1
        win_list_2[m] = win_list[m] + 1

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
marker.forward(3.5 * width)
marker.right(90)
marker.forward(4 * width)
marker.right(180)


height_1 = 0
height_2 = 0
height_3 = 0
height_4 = 0
height_5 = 0
height_6 = 0
height_7 = 0

win_list_1 = []
win_list_2 = []

for i in range (0, 70):
    win_list_1.append(0)
    win_list_2.append(0)

player = 2

win = False
total_moves = 0

while win = False or total_moves < 42:
    guess_1 = 0
    while guess_1 % 1 != or guess_1 < 1 or guess_1 > 7:
        print("")
        guess_1 = input(print("Player 1, choose a column from 1 - 7."))
        guess_1 = float(guess_1)
    guess_1 = int(guess_1)
    
    
    if guess_1 == 1:
        height_1 = height_1 + 1
        str_height = str(height_1)
    elif guess_1 == 2:
        height_2 = height_2 + 1
        str_height = str(height_2)
    elif guess_1 == 3:
        height_3 = height_3 + 1
        str_height = str(height_3)
    elif guess_1 == 4:
        height_4 = height_4 + 1
        str_height = str(height_4)
    elif guess_1 == 5:
        height_5 = height_5 + 1
        str_height = str(height_5)
    elif guess_1 == 6
        height_6 = height_6 + 1
        str_height = str(height_6)
    elif guess_1 == 7:
        height_7 = height_7 + 1
        str_height = str(height_7)
    else:
       print("Something went wrong.")

    height = int(str_height)

    marker.forward(width * guess_1)
    marker.left(90)
    marker.forward(width * height)
    
    marker.width(width)
    marker.forward(1)
    marker.width(1)
    marker.right(180)
    marker.forward(1)
    
    marker.forward(width * height)
    marker.right(90)
    marker.forward(guess_1)
    marker.right(180)
    

    co_ord = column * 10 + row
    player = 3 - player