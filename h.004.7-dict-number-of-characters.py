# Enter a text from the keyboard.
# Put the number of characters in the text in a dictionary.
# The keys of the dictionary should be characters and their values should be their numbers.
# For example, let's say "ankara" is entered as text.
# The dictionary object to be created must contain the following elements.
# {'a': 3, 'n': 1, 'k': 1, 'r': 1}

text = input('enter a text: ')
d = dict()

for t in text:
    c = text.count(t)
    d[t] = c

print(d)
