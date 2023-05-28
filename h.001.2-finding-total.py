# Read a single digit int number from the keyboard.
# (Let this figure be represented by n.) Print the following sum:
# n + nn + nnn + nnnn + nnnnn

n = int(input('enter a single digit int number: '))

result = (1 + 11 + 111 + 1111 + 11111) * n

print(result)
