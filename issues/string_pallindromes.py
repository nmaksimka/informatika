# Задача:
# Дается строка. Необходимо определить является ли она полиндромом. Не учитывать регистр и знаки препинания.
# Данные для тестов:
# Вариант 1 - "А роза упала на лапу Азора!" Ответ: true
# Вариант 2 - "а" Ответ: false
# Вариант 3 - "да"Ответ: false
# Вариант 4 - "" Ответ: "Введена пустая строка!"

tests = (
    "А роза упала на лапу Азора!",
    "а",
    "да",
    ""
)
for i in tests:
    palindromes = i.strip().lower()
    palindromes = palindromes.replace('!', '')
    palindromes = palindromes.replace(' ', '')
    if len(palindromes) == 0:
        print('"Введена пустая строка!"')
    elif len(palindromes) == 1:
        print('false')
    elif palindromes == palindromes[::-1]:
        print('true')
    else:
        print('false')
