def easy_duplicate(num):
    answer = []
    for m in range(1, len(num) + 1):
        answer.append(m)
    print(*answer, sep=',')

def hard_duplicate(num):
    answer = []
    for i in range(len(num)):
        if i + 1 not in answer:
            answer.append(i + 1)

    print(*answer, sep=',')

count = list(map(int, input().split(',')))
easy_duplicate(count)
hard_duplicate(count)
