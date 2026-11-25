alphabet = "abcdefghijklmnopqrstuvwxyz"

text = input("message: ")


def encrypt(text, key):
    result = ""

    for symbol in text:
        if symbol in alphabet:
            position = alphabet.index(symbol)
            new_position = (position + key) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += symbol

    return result


encrypt_message = encrypt(text, 3)

print(encrypt_message)