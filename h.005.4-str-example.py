# Enter a text from the keyboard.
# Then, write the words in that text backwards side by side by placing a single space character between them.
# For example:
# bugün hava      çok       soğuk
# soğuk çok hava bugün

def reversed_text():
    text = input('Enter a text: ')
    splitted_text = text.split()
    reversed_text = ''

    for t in splitted_text[::-1]:
        reversed_text += t + ' '

    return reversed_text


print(reversed_text())

