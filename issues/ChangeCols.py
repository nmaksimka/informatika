n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()]for _ in range(n)]
col = input().split()
k = int(col[0])
l = int(col[1])
for j in matrix:
    j[k], j[l] = j[l], j[k]
answer = list()
for a in range(n):
    raw = []
    for b in range(m):
        raw.append(matrix[a][b])
    answer.append(raw)
for i in range(len(answer)):
    print(*answer[i])