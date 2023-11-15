def caesar_decipher(word):
    result = ""
    for char in word:
        if char.isalpha():
            shift = ord(char) - ord('a') if char.islower() else ord(char) - ord('A')
            new_char = chr((ord(char) + shift) % 26 + ord('a')) if char.islower() else chr((ord(char) + shift) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result

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
def decrypt_text(encrypt_text):
    words = encrypt_text.split()
    decrypted_words = [caesar_decipher(word) for word in words]
    decrypted_text = ' '.join(decrypted_words)
    return decrypted_text

def encrypted_text(descr):
    words = descr.split()
    encrypted_words = [caesar_cipher(word) for word in words]
    encrypt_text = ''.join(encrypted_words)
    return encrypt_text

input_text = input("Введите строку текста на английском языке: ")

print("Зашифрованный текст:", decrypt_text(input_text))
print("Расшифрованный текст:", decrypt_text(encrypted_text(input_text)))