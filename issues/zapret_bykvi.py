def YbratBykvy(word, i):
    if i in word.strip():
        word = word.replace(i, "")
        word = ' '.join(word.split())
    return word


word = input() + ' запретил букву'
letter = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in letter:
    if i in word:
        print(word + ' ' + i)
        word = YbratBykvy(word, i)