# There is a function called islice in the itertools module.
# The parametric structure of the function is as follows:
#
# islice(iterable, start, stop=None, step=1)
#
# Write the islice function in the form of a generator function.

def myislice(iterable, start, stop=None, step=1):
    result = []
    if stop is None:
        start = 0
        stop = start
    if stop > len(iterable):
        stop = len(iterable)
    i = start
    while i < stop:
        result.append(iterable[i])
        i += step
    yield result


a = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
for c in myislice(a, start=1, stop=5, step=1):
    print(c, end=' ')
