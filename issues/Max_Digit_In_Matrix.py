def create_matrix():
    matrix = []
    for _ in range(n):
        raw = []
        raw = list(map(int, input().split()))
        matrix.append(raw)
    return matrix


n = int(input())
m = int(input())
matrix = create_matrix()
Elem = max(max(matrix, key=max))
answer = []
MinI = []
MinJ = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == Elem:
            answer.append(i)
            answer.append(j)
            break
    else:
        continue
    break

print(*answer)

# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# row, col = 0, 0
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
#
# print(row, col)