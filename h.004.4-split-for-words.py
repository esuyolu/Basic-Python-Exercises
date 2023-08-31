# Read a text from the keyboard.
# Put the words in the text in a list and print the list.

text = input('enter a text: ')

words = []
i = 0

while True:
    while i < len(text) and not text[i].isalnum():
        i += 1
    if i == len(text):
        break
    start = i
    while i < len(text) and text[i].isalnum():
        i += 1
    words.append(text[start:i])
    if i == len(text):
        break

print(words)
