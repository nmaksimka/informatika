nm = input().split()
n = int(nm[0])
m = int(nm[1])
matrix = [[0 for _ in range(m)] for _ in range(n)]

top_row = 0
bottom_row = n - 1
left_col = 0
right_col = m - 1
counter = 1
direction = 0

while top_row <= bottom_row and left_col <= right_col:
    if direction == 0:
        for i in range(left_col, right_col + 1):
            matrix[top_row][i] = counter
            counter += 1
        top_row += 1

    elif direction == 1:
        for i in range(top_row, bottom_row + 1):
            matrix[i][right_col] = counter
            counter += 1
        right_col -= 1

    elif direction == 2:
        for i in range(right_col, left_col - 1, -1):
            matrix[bottom_row][i] = counter
            counter += 1
        bottom_row -= 1

    elif direction == 3:
        for i in range(bottom_row, top_row - 1, -1):
            matrix[i][left_col] = counter
            counter += 1
        left_col += 1

    direction = (direction + 1) % 4


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
