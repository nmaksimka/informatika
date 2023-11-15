import random

dic = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
       'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила']

word = list(random.choice(dic))
word2 = list('-' * len(word))
s = 'Эти буквы ты уже пробовал: '
c = 0

hangman_figures = {
    1: '''
 O 
''',
    2: '''
 O 
 |
''',
    3: '''
 O 
/|
''',
    4: '''
 O 
/|\\
''',
    5: '''
 O 
/|\\
/
''',
    6: '''
 O 
/|\\
/ \\
'''
}

print('Какое слово я загадал?')
print(*word2)
print('Гадай по буквам=)')

while '-' in word2:
    letter = input()
    s += letter.upper() + ' '
    print(s)

    if letter in word:
        while letter in word:
            word2[word.index(letter)] = letter.upper()
            word[word.index(letter)] = '-'
        print(*word2)
    else:
        c += 1
        print(hangman_figures.get(c))

        if c == 6:
            print('Ты проиграл=)')
            break
else:
    print('Ты победил, поздравляю!')
