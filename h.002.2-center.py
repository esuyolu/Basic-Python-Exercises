# Read a text and an int number from the keyboard.
# Center the text you entered without using the center method of the str class,
# with spaces relative to the int number you entered.

text = input("enter a text: ")
number = int(input("enter an int number: "))

text_count = len(text)
left_space_count = (number - text_count) // 2
right_space_count = number - (text_count + left_space_count)

result = ' ' * left_space_count + text + ' ' * right_space_count

print(':', result, ':', sep='')
