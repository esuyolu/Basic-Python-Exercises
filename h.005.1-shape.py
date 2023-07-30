# Write a function named disp_shape that takes an int value as a parameter and prints the following pattern:
#
#  1 2 3 4 5
#   2 3 4 5
#    3 4 5
#     4 5
#      5
#     4 5
#    3 4 5
#   2 3 4 5
#  1 2 3 4 5

def disp_shape(n):
    for i in range(0, n):
        for k in range(i):
            print(' ', end='')
        for j in range(i + 1, n + 1):
            print(j, end=' ')
        print()

    for i in range(0, n - 1):
        for k in range(i + 1, n - 1):
            print(' ', end='')
        for j in range(n - i - 1, n + 1):
            print(j, end=' ')
        print()


n = int(input('enter a number: '))
disp_shape(n)
