def caesar_cipher(word):
    result = ""
    for char in word:
        if char.isalpha():
            shift = ord(char) - ord('a') if char.islower() else ord(char) - ord('A')
            new_char = chr((ord(char) - shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - shift) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result
def encrypt_text(input_text):
    words = input_text.split()
    encrypted_words = [caesar_cipher(word) for word in words]
    encrypted_text = ' '.join(encrypted_words)
    return encrypted_text

input_text = input("Введите строку текста на английском языке: ")

print("Зашифрованный текст:", encrypt_text(input_text))