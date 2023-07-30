# The Armstrong number is a number whose sum of the cubes of its digits is equal to the number itself.
# So, for example, x^3+y^3+z^3 = xyz, where xyz is a three-digit number.
# For example, the number 153 is an Armstrong number.
# Because 1^3 + 5^3 + 3^3 = 153.
# Write a function called is_armstrong that returns
# whether the number it receives with its parameter is Armstrong.

def is_armstrong(n):
    digits = get_digits(n)
    sum_of_cubes_of_digits = 0

    for i in range(len(digits)):
        sum_of_cubes_of_digits += digits[i] ** 3

    return n == sum_of_cubes_of_digits


def get_digits(num):
    digits = []
    while num:
        digits.append(num % 10)
        num //= 10
    return digits


# Control
while True:
    a = int(input('Enter a number: '))
    if a == 0:
        break
    print('Armstrong' if is_armstrong(a) else 'Not Armstrong')
