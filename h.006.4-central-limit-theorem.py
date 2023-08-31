from random import sample
from statistics import mean


def get_central_limit_theorem(n):
    frequency_dict = {0: range(0, 1000), 1: range(1000, 2000), 2: range(2000, 3000), 3: range(3000, 4000),
                      4: range(4000, 5000),
                      5: range(5000, 6000), 6: range(6000, 7000), 7: range(7000, 8000), 8: range(8000, 9000),
                      9: range(9000, 10000)}

    frequency_value_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for _ in range(n):
        value = int(mean(sample(range(10000), 5)))
        for k, v in frequency_dict.items():
            if value in v:
                frequency_value_list[k] += 1

    for i in range(10):
        print(frequency_dict[i], '      ', end='')
        for _ in range(frequency_value_list[i] // 30):
            print('X', end='')
        print()


get_central_limit_theorem(5000)
