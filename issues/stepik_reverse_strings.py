def digit(dig):
    if len(dig) == 5:
        return dig[::-1].strip('0')
    elif len(dig) == 6:
        if '0' in dig and dig[-1] != '0':
            return (dig[0] + dig[-1] + dig[-2:-6:-1]).strip('0')
        else:
            return dig[0] + dig[-1] + dig[-2:-6:-1]


input_value = input()
result = digit(input_value)
print(result)