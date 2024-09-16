def create_matrix(nm):
    matrix = []
    for k in range(nm):
        matrix.append(list(map(int, input().split())))
    return matrix

size = int(input())
answer = []
matrix = create_matrix(size)

for i in range(size):
    for j in range(size):
        if i >= j and i <= size - 1 - j or i <= j and i >= size - 1 - j:
            answer.append(matrix[i][j])
print(max(answer))