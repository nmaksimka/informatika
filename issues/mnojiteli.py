n = int(input())
def mnojiteli():
    l = list()
    for i in range(n):
        x = int(input())
        l.append(x)
    answer = int(input())
    for j in range(len(l)):
        for k in range(len(l)):
            if l[j] * l[k] == answer and j != k:
                return "ДА"
    return "НЕТ"
print(mnojiteli())