digit = int(input())
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
def coordinate(x):
    x = list(x)
    if 0 not in x:
        if x[0] < 0 and x[1] < 0:
            return 3
        elif x[0] < 0 and x[1] > 0:
            return 2
        elif x[0] > 0 and x[1] > 0:
            return 1
        elif x[0] > 0 and x[1] < 0:
            return 4
    else:
        return 0



for i in range(digit):
    x = map(int, input().split())
    answer = coordinate(x)
    if answer == 1:
        counter1 += 1
    elif answer == 2:
        counter2 += 1
    elif 3 == answer:
        counter3 += 1
    elif 4 == answer:
        counter4 += 1
print("Первая четверть:", counter1)
print("Вторая четверть:", counter2)
print("Третья четверть:", counter3)
print("Четвертая четверть:", counter4)