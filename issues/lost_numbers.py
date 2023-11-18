old_numbers = input().split()
sorted_numbers = sorted(old_numbers)
new_numbers = []
x = sorted_numbers[-1]
for i in range(1, int(x) + 1):
    if str(i) not in old_numbers:
        new_numbers.append(i)
print(*new_numbers)