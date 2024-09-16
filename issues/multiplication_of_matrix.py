nm1 = input().split()
n1, m1 = int(nm1[0]), int(nm1[1])
matrix1 = []
matrix2 = []
counter = 0
for i in range(n1):
    matrix1.append(input().split())
ghost = input()

nm2 = input().split()
n2, m2 = int(nm2[0]), int(nm2[1])
for i in range(n2):
    matrix2.append(input().split())

matrix = [[0 for _ in range(m2)]for _ in range(n1)]
counter = 0

for i in range(n1):
    for j in range(m2):
        digit = 0
        for k in range(m1):
            digit += int(matrix1[i][k]) * int(matrix2[k][j])
        matrix[i][j] = digit


for i in range(n1):
    for j in range(m2):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()