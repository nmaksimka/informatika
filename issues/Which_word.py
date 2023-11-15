from random import *

# алгоритм игры
def guessing_game(x, y, z):
    phrases_too_much = ['Ох, слишком много! Попробуй еще раз', 'Многовато будет!', 'Ого-го, это слишком много!',
                        'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!']
    phrases_too_little = ['Ох, слишком мало! Попробуй еще раз', 'Маловато будет!', 'Эх, это слишком мало!',
                        'Мало!', 'Бери выше', 'Маловато!', 'Нужно большее число!']
    phrases_almost = ['Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок', 'Ты уже рядом', 'Ну же, почти',
                      'Горячо!']
    phrases_guessed = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)']
    phrases_too_soon = ['Ого, так быстро!', 'Да ты волшебник! Ты угадал моё число', 'Скажи честно, ты подглядывал?',
                        'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!']
    if x > y:
        x, y = y, x
        num_0 = randint(x, y)
        print('Я загадал число от', x, 'до', y, 'Попробуй угадать!')
    else:
        num_0 = randint(x, y)
        print('Я загадал число от', x, 'до', y, 'Попробуй угадать!')
    count = 0
    z = int(z)
    while True:
        num_1 = int(input())
        count += 1
        z -= 1
        if z == 0:
            print('Ты проиграл тупой баклажан')
            break
        elif num_1 == num_0:
            if count == 1:
                print('Скажи честно, ты подглядывал?')
                if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
                    start()
                else:
                    print('Приходи, когда появится желание сыграть снова :)')
                    break
            elif 1 <= count <= z // 2:
                print(choice(phrases_too_soon))
                if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
                    start()
                else:
                    print('Приходи, когда появится желание сыграть снова :)')
                    break
            else:
                print(choice(phrases_guessed))
                if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
                    start()
                else:
                    print('Приходи, когда появится желание сыграть снова :)')
                    break
        elif num_1 > num_0:
            if abs(num_1 - num_0) < 5:
                print(choice(phrases_too_much), choice(phrases_almost), sep='\n')
            else:
                print(choice(phrases_too_much))
        elif num_1 < num_0:
            if abs(num_1 - num_0) < 5:
                print(choice(phrases_too_little), choice(phrases_almost),  sep='\n')
            else:
                print(choice(phrases_too_little))

# описание правил
def game_rules():
    print('Отлично! Давай ознакомлю тебя с правилами игры.')
    print('Я загадаю число, а ты будешь его отгадывать.')
    print('Диапазон чисел ты выберешь сам.')
    print('К примеру, если ты укажешь диапазон чисел от 0 до 100, я не смогу загадать число "101" :)')
    print('Я попрошу тебя ввести границы диапазона. Границы не должны совпадать! Так играть мы не сможем.')
    input('А теперь напиши что-нибудь, чтобы я был уверен, что ты понял правила игры :)')

# проверка правильности
def is_valid_z(z):
    if z.isdigit() is False:
        print('Ты ввел не число :(')
        print('Попробуй включить мозг и ввести число')
    elif int(z) < 1:
        print('Больной?')
        start()


def is_valid_x(x):
    if x.isdigit() is False:
        print('Ты ввел не число :(')
        print('Что ж, ладно, введи новые числа.')
        start()

def is_valid_xy(x, y):
    while x == y:
        print('Ты ввел одинаковые числа. Я же говорил, что так играть мы не сможем :(')
        print('Что ж, ладно, введи новое число.')
        start()
    if y.isdigit() is False:
        print('Я запутался :( Это не число')
        print('Давай заново :)')
        start()
    else:
        return True

# запуск игры
def start():
    x = input('Введи первую границу диапазона: ')
    is_valid_x(x)
    y = input('Введи вторую границу диапазона: ')
    z = input('Введи желаемое количество попыток:')
    is_valid_z(z)
    if is_valid_xy(x, y) is True:
        x, y = int(x), int(y)
        guessing_game(x, y, z)

# приглашение в игру
if input('Приветствую тебя в угадайке! Не желаешь сыграть в игру? Введи "да" или "нет" ').lower() in ['да', 'lf']:
    game_rules()
    start()
else:
    if input('Это не займёт много времени и сил. Если всё таки надумал, введи "да" :)').lower() in ['да', 'lf']:
        game_rules()
        start()
    else:
        print('Приходи, когда появится желание сыграть :)')