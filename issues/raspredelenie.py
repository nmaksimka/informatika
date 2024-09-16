def raspredelenie(string):
    answer = [[]]
    for i in range(len(string) + 1):
        for l in range(len(string) - i):
            answer.append(string[l:l + i + 1])
    return answer


print(raspredelenie(input().split(' ')))