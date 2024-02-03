def read_csv(path, sep=',', skiprows=0, converter={}):
    with open(path, 'r', encoding='utf-8') as f:
        i = 0
        list = []
        for line in f:
            i += 1
            if i <= skiprows:
                continue

            a = line[:-1].split(sep)
            if a[0] == '':
                continue
            if converter is not None:
                for key, value in converter.items():
                    a[key] = value(a[key])

            list.append(a)

    return list


list = read_csv('test.txt', ',"', 1, {1: int, 2: float})
print(list)
