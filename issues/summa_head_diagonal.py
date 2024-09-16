def create_matrix(nm):
    matrix = []
    for k in range(nm):
        matrix.append(list(map(int, input().split())))
    return matrix

size = int(input())
answer = 0
matrix = create_matrix(size)
for i in range(size):
    answer += matrix[i][i]
print(answer)