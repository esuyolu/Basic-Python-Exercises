# Enter a number which is n from the keyboard.
# Print numbers with even digits from 0 to n (including n).
# For example, even if the value 5000 is entered from the keyboard,
# all digits of all numbers to be printed must be even (0, 2, 4, 8, 22, 24, ... 4882, ....).

n = int(input('enter a number: '))

for i in range(n + 1):
    flag = True
    val = i
    while val != 0:
        digit = val % 10
        if digit % 2 != 0:
            flag = False
            break
        val //= 10
    if flag:
        print(i, end=' ')


