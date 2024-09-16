queen = input()
letter = queen[0]
digit = queen[1]
matrix = [['.' for _ in range(8)] for _ in range(8)]
digits = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
matrix[digits[digit]][letters[letter]] = matrix[digits[digit]][letters[letter]].replace('.', 'Q')
for i in range(8):
    for j in range(8):
        matrix[digits[digit]][j] = matrix[digits[digit]][j].replace('.', '*')
        matrix[i][letters[letter]] = matrix[i][letters[letter]].replace('.', '*')
        if i == digits[digit] or j == letters[letter] or abs(digits[digit] - i) == abs(letters[letter] - j):
            matrix[i][j] = matrix[i][j].replace('.', '*')

for i in range(8):
    print(*matrix[i])