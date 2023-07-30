# Read a text from the keyboard.
# Put the words in the text in a list and print the list.

text = input('enter a text: ')

result = []
res = ''

for t in text:
    if t.isalpha():
        res += t
    else:
        if res != '':
            result.append(res)
            res = ''

print(result)
