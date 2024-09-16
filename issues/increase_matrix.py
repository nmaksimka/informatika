def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix1[0])):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

def matrix_power(matrix, power):
    result = matrix.copy()
    for _ in range(power - 1):
        result = matrix_multiply(result, matrix)
    return result

nm = input().split()
n = int(nm[0])
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
power = int(input())

result = matrix_power(matrix, power)
for row in result:
    print(*row)
