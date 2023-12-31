#Задача:
#На вход подается строка с различными символами, цифрами и знаками. Необходимо используя регулярные выражения вывести отдельно цифры, буквы и знаки и подсчитать их.
#Тесты:
#Вариант 1: "Привет! Меня зовут Влад! Мне 15, я родился в 2005 году. А ты?"
#Ответ:
#Буквы: П,р,и,в,е,т,М,е,н,я,з,о,в,у,т,В,л,а,д,М,н,е,я,р,о,д,и,л,с,я,в,г,о,д,у,А,т,ы  Всего: 38
#: 1,5,2,0,0,5 Всего: 6
#Символы: !,!,,,.,? Всего: 5
#Пробелов всего: 12

tests = [
    "Привет! Меня зовут Влад! Мне 15, я родился в 2005 году. А ты?"
]

for k in tests:
    counter_b = 0
    counter_d = 0
    counter_s = 0
    counter_p = 0
    l_b = []
    l_d = []
    l_s = []
    for i in k:
        if i.lower() in '[а-яё]+|[a-z]+':  # or i.lower() in ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё']:
            l_b.append(i + ',')
            counter_b += 1
        elif i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            l_d.append(i + ',')
            counter_d += 1
        elif i in ['!', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']:
            l_s.append(i + ',')
            counter_s += 1
        elif i == ' ':
            counter_p += 1

    print('Буквы:', *l_b, 'Всего:', counter_b)
    print('Цифры:', *l_d, 'Всего:', counter_d)
    print('Символы:', *l_s, 'Всего:', counter_s)
    print('Пробелов всего:', counter_p)