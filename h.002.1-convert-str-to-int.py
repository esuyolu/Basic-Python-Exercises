# Read a 3-digit int type numeric text from the keyboard.
# Print the text by converting it to an int number without using the int function.

values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

n = input('enter a 3-digit int type numeric text: ')

result = values[n[0]] * 100 + values[n[1]] * 10 + values[n[2]] * 1

print('result: ', result)
print(result * result)
