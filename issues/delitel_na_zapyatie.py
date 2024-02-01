def delitelnazapyatie():
    t = input()
    answer = ''
    counter = 0
    for i in t[::-1]:
        answer += i
        counter += 1
        if counter == 3:
            counter = 0
            answer += ','
    print(answer[::-1].strip(','))

delitelnazapyatie()