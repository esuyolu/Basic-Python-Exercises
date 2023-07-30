# Write a function named disp_char_pattern that takes a character as a parameter
# (the character can be uppercase or lowercase) and prints the following pattern:
# For ch = F
#
#        A
#       B B
#      C   C
#     D     D
#    E       E
#   F         F
#    E       E
#     D     D
#      C   C
#       B B
#        A

def disp_char_pattern(ch):
    num = ord(ch) - ord('0')
    first_num = ord('A') - ord('0')

    for i in range(num - first_num + 1):
        for j in range(num - first_num - i, 0, -1):
            print(' ', end='')
        print(chr(ord('0') + i + first_num), end='')
        for t in range(0, 2 * i - 1):
            print(' ', end='')

        if i == 0:
            print()
            continue

        print(chr(ord('0') + i + first_num))

    for i in range(num - first_num):
        for j in range(0, i + 1):
            print(' ', end='')
        print(chr(ord('0') + num - i - 1), end='')
        for t in range((num - first_num - i) * 2 - 3):
            print(' ', end='')

        if i == num - first_num - 1:
            print()
            continue

        print(chr(ord('0') + num - i - 1))


ch = input('Enter a character: ')
print()
disp_char_pattern(ch)
