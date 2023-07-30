# Write a function named crown that outputs the following pattern.
# For n = 4
#
# 1        1        1
# 12      212      21
# 123    32123    321
# 1234  4321234  4321
# 1234554321234554321

def crown(n):
    for i in range(1, n + 2):
        for k in range(1, i + 1):
            print(k, end='')
        for j in range((n - i + 1) * 2):
            print(' ', end='')
        for t in range(i, 0, -1):
            print(t, end='')
        for s in range(2, i + 1):
            print(s, end='')
        for j in range((n - i + 1) * 2):
            print(' ', end='')
        for r in range(i, 0, -1):
            print(r, end='')

        print()


n = int(input('enter a number: '))
print()
crown(n)
