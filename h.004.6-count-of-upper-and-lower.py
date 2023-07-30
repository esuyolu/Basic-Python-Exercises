# Enter a text from the keyboard,
# print how many uppercase letters and lowercase letters are in the text.
# (Non-alphabetic characters in the text will be ignored.)

text = input('enter a text: ')
count_of_upper = 0
count_of_lower = 0

for t in text:
    if t.isupper():
        count_of_upper += 1
    elif t.islower():
        count_of_lower += 1

print(f'There are {count_of_upper} uppercase letters in the text.')
print(f'There are {count_of_lower} lowercase letters in the text.')
