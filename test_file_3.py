win_game_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (0, 57):
    if i < 24:
        win_type = "horizontal"
    elif i >= 24 and i < 45:
        win_type = "vertical"
    elif i >= 45 and i < 57:
        win_type = "diagonal"
    else:
        win_type = None

    if win_type == "horizontal":
        rem = i % 4
        quot = int((i - rem)/6)
        a = quot + 1
        b = rem + 1
        c = rem + 4
    elif win_type == "vertical":
        rem = i % 7
        quot = int((i - rem)/3)
        a = quot + 1
        b = quot + 4
        c = rem + 1



for j in range (0, 24):
    rem = i % 4
    quot = int((i - rem)/6)
    a = quot + 1
    b = rem + 1
    c = rem + 4

    if row == a and column >= b and column <= c:
        x = win_game_list[j]
        x = x + 1
        win_game_list[j] = x
    else:
        toggle = False

for k in range (0, 21):
    rem = i % 7
    quot = int((i - rem)/3)
    a = quot + 1
    b = quot + 4
    c = rem + 1
    k = k + 24

    if row >= a and row <= b and column == c:
        x = win_game_list[k]
        x = x + 1
        win_game_list[k] = x
    else:
        toggle = False

    k = k - 24

for l in range (0, 12):
    rem = l % 4
    quot = s




if row == 1 and column >= 1 and column < 5:
    x = win_game_list[0]
    x = x + 1
    win_game_list[0] = x
if row == 1 and column >= 2 and column < 6:
    x = win_game_list[1]
    x = x + 1
    win_game_list[1] = x
if row == 1 and column >= 3 and column < 7:
    x = win_game_list[2]
    x = x + 1
    win_game_list[2] = x
