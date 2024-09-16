def create_matrix(nm):
    matrix = []
    for k in range(nm):
        matrix.append(list(map(int, input().split())))
    return matrix


size = int(input())
answer = []
matrix = create_matrix(size)
raw1 = []
raw2 = []
raw3 = []
raw4 = []

for i in range(size):
    for j in range(size):
        if i < j and i < size - 1 - j:
            raw1.append(matrix[i][j])
        elif i < j and i > size - 1 - j:
            raw2.append(matrix[i][j])
        elif i > j and i > size - 1 - j:
            raw3.append(matrix[i][j])
        elif i > j and i < size - 1 - j:
            raw4.append(matrix[i][j])

print("Верхняя четверть:", sum(raw1))
print("Правая четверть:", sum(raw2))
print("Нижняя четверть:", sum(raw3))
print("Левая четверть:", sum(raw4))