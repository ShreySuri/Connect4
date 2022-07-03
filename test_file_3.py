win_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

co_ord = column * 10 + row


def add_to_list(a, b, c, d, e, f, g, h, i, j, k, l, m):
    win_list[a] = win_list[a] + 1
    win_list[b] = win_list[b] + 1
    win_list[c] = win_list[c] + 1
    win_list[d] = win_list[d] + 1
    win_list[e] = win_list[e] + 1
    win_list[f] = win_list[f] + 1
    win_list[g] = win_list[g] + 1
    win_list[h] = win_list[h] + 1
    win_list[i] = win_list[i] + 1
    win_list[j] = win_list[j] + 1
    win_list[k] = win_list[k] + 1
    win_list[l] = win_list[l] + 1
    win_list[m] = win_list[m] + 1
    











if co_ord == 11:
    add_to_list(0, 24, 45, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68)
elif co_ord == 21:
    add_to_list(0, 1, 27, 46, 68, 68, 68, 68, 68, 68, 68, 68, 68)
elif co_ord == 31:
    add_to_list(0, 1, 2, 30, 47, 68, 68, 68, 68, 68, 68, 68, 68)
elif co_ord == 41:
    add_to_list(0, 1, 2, 3, 33, 48, 56, 68, 68, 68, 68, 68, 68)
elif co_ord == 51:
    add_to_list(1, 2, 3, 36, 57, 68, 68, 68, 68, 68, 68, 68, 68)
elif co_ord == 61:
    add_to_list(2, 3, 39, 58, 68, 68, 68, 68, 68, 68, 68, 68, 68)
elif co_ord == 71:
    add_to_list(3, 42, 59, 68, 68, 68, 68, 68, 68, 68, 68,  68, 68)
elif co_ord == 12:
    add_to_list(4, 24, 25, 49, 68, 68, 68, 68, 68, 68, 68, 68, 68)
elif co_ord == 22:
    add_to_list(4, 5, 27, 28, 45, 50, 68, 68, 68, 68, 68, 68, 68)
elif co_ord == 32:
    add_to_list(4, 5, 6, 30, 31, 46, 51, 56, 68, 68, 68, 68, 68)
elif co_ord == 42:
    
elif co_ord == 52:

elif co_ord == 62:

elif co_ord == 72:





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
    quot = int((i - rem)/3)
    co_ord = quot * 10 + rem
    co_ord = co_ord + 11
    a = co_ord % 11
    b = co_ord + 33

    if 



