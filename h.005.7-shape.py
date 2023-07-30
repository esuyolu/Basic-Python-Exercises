# Write a function called print_shape that takes an int value as a parameter and prints the following pattern:
# For n = 5
#
#    **********
#    ****  ****
#    ***    ***
#    **      **
#    *        *
#    *        *
#    **      **
#    ***    ***
#    ****  ****
#    **********

def print_shape(n):
    for i in range(n):
        for j in range(n - i, 0, - 1):
            print('*', end='')
        for k in range(i * 2):
            print(' ', end='')
        for j in range(n - i, 0, - 1):
            print('*', end='')
        print()
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('*', end='')
        for k in range((n - i) * 2):
            print(' ', end='')
        for j in range(1, i + 1):
            print('*', end='')
        print()


n = int(input('Enter a number: '))
print()
print_shape(n)
