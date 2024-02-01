def maximum_number(l):
    x = 0
    for i in l:
        for j in l:
            if j > i:
                x = j
    return x
