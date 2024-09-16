nm = input().split()
n, m = int(nm[0]), int(nm[1])
matrix1 = []
matrix2 = []
counter = 0
for i in range(n):
    matrix1.append(input().split())
ghost = input()
for i in range(n):
    matrix2.append(input().split())

matrix = [[i for i in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(2), end='')
    print()