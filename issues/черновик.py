with open(input(), encoding='utf-8') as file, open('forbidden_words.txt', encoding='utf-8') as nezya:
    line = file.read()
    s_lower = line.lower()
