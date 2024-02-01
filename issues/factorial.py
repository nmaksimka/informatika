def FindFactorial(n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1
        for i in range(1, n + 1):
            x *= i
        return x
    else:
        x = 1
        for i in range(1, n + 1):
            x *= i
        return x
def FindFactorialnerecursia(n):
    if n == 0:
        print(1)
    elif n < 0:
        x = 1
        for i in range(1, n + 1):
            x *= i
        print(x)
    else:
        x = 1
        for i in range(1, n + 1):
            x *= i
        print(x)
digit = int(input())
otvet = FindFactorial(digit)
print(otvet)
FindFactorialnerecursia(digit)