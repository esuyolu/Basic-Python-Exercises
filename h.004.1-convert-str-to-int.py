# Read a string of numeric characters from the keyboard with the input function.
# Without using the int function, convert the text to an int value and print it multiplied by 2.
# Space characters can be found at the beginning and end of the text.
# These characters should not break the execution of your code.

value = input('Please enter a text consisting of numeric characters: ')

result = 0

for c in value:
    if not c.isspace():
        num = ord(c) - ord('0')
        result = result * 10 + num

print(result * 2)
