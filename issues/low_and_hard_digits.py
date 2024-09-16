nums = [i for i in range(1, 1000+1)]

def prostye(num):
    if num == 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def slozhnye(num):
    if num == 1:
        return False
    for i in range(2, num+1):
        if (num % i) == 0:
            return True


print(f'Простые: {list(filter(prostye, nums))}')
print(f'Сложные: {list(filter(slozhnye, nums))}')