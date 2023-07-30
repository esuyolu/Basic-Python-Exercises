# Read an int number from the keyboard.
# Convert the number to text without using the str function.

value = int(input('Please enter a number: '))

result = ''

while value:
    val = value % 10
    c = chr(ord('0') + val)
    result += c
    value //= 10

result = result[::-1]

print('str of value: ' + result)
