def somayaji_pi(n):
    result = 3
    for i in range(1, n + 1):
        num = 2 * i + 1
        if i % 2 != 0:
            result += 4 / (num ** 3 - num)
        else:
            result -= 4 / (num ** 3 - num)

    return result


n = int(input('Enter a number: '))
print(somayaji_pi(n))
