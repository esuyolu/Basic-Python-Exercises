def bailey_borwein_plouffe_pi(k):
    result = 0
    for i in range(k + 1):
        result += ((1 / 16) ** i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))

    return result


num = int(input('Enter a number: '))
print(bailey_borwein_plouffe_pi(num))
