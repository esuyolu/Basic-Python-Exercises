# Read a number n from the keyboard and write the program that creates the following pattern
# (n = 6 in our example):
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

n = int(input('enter a number: '))

for i in range(n):
    for j in range(n - 1 - i):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()

n -= 1
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(' ', end='')
        j += 1
    k = 1
    while k <= (2 * (n - i) + 1):
        print('*', end='')
        k += 1
    i += 1
    print()
