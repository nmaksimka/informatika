def can_return_to_origin(string):
    if ((string.count('N') > 0) == (string.count('S') > 0)) and ((string.count('W') > 0) == (string.count('E') > 0)):
        return "Yes"
    return "No"


print(can_return_to_origin(input().upper().strip()))