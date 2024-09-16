def create_matrix():
    matrix = []
    for k in range(n):
        raw = []
        for l in range(m):
            raw.append(input())
        matrix.append(raw)
    return matrix


n = int(input())
m = int(input())
matrix = create_matrix()
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
print()
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()