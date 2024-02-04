def myrepeat(val, times=None):
    i = 0

    if times is None:
        while True:
            yield val

    while i < times:
        yield val
        i += 1


for x in myrepeat(10, 5):
    print(x, end=' ')