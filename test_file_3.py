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
    add_to_list(0, 24, 45, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 21:
    add_to_list(0, 1, 27, 46, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 31:
    add_to_list(0, 1, 2, 30, 47, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 41:
    add_to_list(0, 1, 2, 3, 33, 48, 57, 69, 69, 69, 69, 69, 69)
elif co_ord == 51:
    add_to_list(1, 2, 3, 36, 58, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 61:
    add_to_list(2, 3, 39, 59, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 71:
    add_to_list(3, 42, 60, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 12:
    add_to_list(4, 24, 25, 49, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 22:
    add_to_list(4, 5, 27, 28, 45, 50, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 32:
    add_to_list(4, 5, 6, 30, 31, 46, 51, 56, 69, 69, 69, 69, 69)
elif co_ord == 42:
    add_to_list(4, 5, 6, 7, 33, 34, 47, 52, 57, 61, 69, 69, 69)
elif co_ord == 52:
    add_to_list(5, 6, 7, 36, 37, 48, 58, 62, 69, 69, 69, 69, 69)
elif co_ord == 62:
    add_to_list(6, 7, 39, 40, 59, 63, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 72:
    add_to_list(7, 42, 43, 64, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 13:
    add_to_list(8, 24, 25, 26, 53, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 23:
    add_to_list(8, 9, 27, 28, 29, 49, 54, 57, 69, 69, 69, 69, 69)
elif co_ord == 33:
    add_to_list(8, 9, 10, 30, 31, 32, 45, 50, 55, 58, 61, 69, 69)
elif co_ord == 43:
    add_to_list(8, 9, 10, 11, 33, 34, 35, 46, 51, 56, 59, 62, 65)
elif co_ord == 53:
    add_to_list(9, 10, 11, 36, 37, 38, 47, 52, 60, 63, 66, 69, 69)
elif co_ord == 63:
    add_to_list(10, 11, 39, 40, 41, 48, 64, 67, 69, 69, 69, 69, 69)
elif co_ord == 73:
    add_to_list(11, 42, 43, 44, 68, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 14:
    add_to_list(12, 24, 25, 26, 57, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 24:
    add_to_list(12, 13, 27, 28, 29, 53, 58, 61, 69, 69, 69, 69, 69)
elif co_ord == 34:
    add_to_list(12, 13, 14, 30, 31, 32, 49, 54, 59, 62, 65, 69, 69)
elif co_ord == 44:
    add_to_list(12, 13, 14, 15, 33, 34, 35, 45, 50, 55, 60, 63, 66)
elif co_ord == 54:
    add_to_list(13, 14, 15, 36, 37, 38, 46, 51, 56, 64, 67, 69, 69)
elif co_ord == 64:
    add_to_list(14, 15, 39, 40, 41, 47, 52, 68, 69, 69, 69, 69, 69)
elif co_ord == 74:
    add_to_list(15, 42, 43, 44, 48, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 15:
    add_to_list(16, 25, 26, 61, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 26:
    add_to_list(16, 17, 28, 29, 62, 65, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 36:
    add_to_list(16, 17, 18, 31, 32, 53, 63, 66, 69, 69, 69, 69, 69)
elif co_ord == 46:
    add_to_list(16, 17, 18, 19, 34, 35, 49, 54, 64, 67, 69, 69, 69)
elif co_ord == 56:
    add_to_list(17, 18, 19, 37, 38, 50, 55, 68, 69, 69, 69, 69, 69)
elif co_ord == 66:
    add_to_list(18, 19, 40, 41, 51, 56, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 76:
    add_to_list(19, 43, 44, 52, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 17:
    add_to_list(20, 26, 65, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 27:
    add_to_list(20, 21, 29, 66, 69, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 37:
    add_to_list(20, 21, 22, 32, 67, 69, 69, 69, 69, 69, 69, 69, 69)
elif co_ord == 47:
    add_to_list(20, 21, 22, 23, 35, 53, 68, 69, 69, 69, 69, 69, 69)