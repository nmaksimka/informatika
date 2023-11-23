def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

def main():
    text = input("Введите текст для шифрования: ")
    shift = int(input("Введите сдвиг для шифра Цезаря: "))

    # Шифрование
    encrypted_text = caesar_cipher(text, shift)
    print(f"Зашифрованный текст: {encrypted_text}")

    # Дешифрование
    decrypted_text = caesar_decipher(encrypted_text, shift)
    print(f"Расшифрованный текст: {decrypted_text}")

if __name__ == "__main__":
    main()
