Timur = input()
Ruslan = input()
def kmb(a, b):
    if a == "камень" and b == "ножницы":
        return 'Тимур'
    elif a == "ножницы" and b == "бумага":
        return 'Тимур'
    elif a == "бумага" and b == "камень":
        return "Тимур"
    elif a == b:
        return "ничья"
    else:
        return "Руслан"


print(kmb(Timur, Ruslan))