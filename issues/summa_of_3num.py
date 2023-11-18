def find_position(all_num):
    position = []
    l = len(all_num)
    for i in range(l):
        if i + 3 < l and all_num[i] + all_num[i + 1] + all_num[i + 2] == all_num[i + 3]:
            position.append(i)
            position.append(i + 1)
            position.append(i + 2)
    return position

all_num = list(map(int, input().split(',')))
otvet = find_position(all_num)
print(*otvet)
