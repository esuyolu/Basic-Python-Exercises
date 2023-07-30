import math


def newton_pi(k):
    result = 0
    for i in range(k + 1):
        result += (2 ** (i + 1) * math.factorial(i) ** 2) / (math.factorial(2 * i + 1))

    return result


num = int(input('Enter a number: '))
print(newton_pi(num))
