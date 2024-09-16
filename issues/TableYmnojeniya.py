def create_matrix(n, m):
    mult = []
    for i in range(n):
        raw = []
        for j in range(m):
            raw.append(i * j)
        mult.append(raw)
    return mult

n = int(input())
m = int(input())
matrix = create_matrix(n, m)
for raw in matrix:
    print(*raw)
