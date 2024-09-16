def create_matrix(nm):
    matrix = []
    for k in range(nm):
        matrix.append(list(map(int, input().split())))
    return matrix

size = int(input())
answer = 0
matrix = create_matrix(size)

for row in matrix:
    row_sum = sum(row)
    row_avg = row_sum / len(row)
    answer = 0
    for element in row:
        if element > row_avg:
            answer += 1
    print(answer)