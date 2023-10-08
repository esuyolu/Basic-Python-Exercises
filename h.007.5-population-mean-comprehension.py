import itertools
import statistics

a = [1, 2, 3, 4, 5]
b = [itertools.combinations(a, i) for i in range(1, len(a) + 1)]
c = []

for i in b:
    for j in i:
        c.append(list(j))

d = [statistics.mean(i) for i in c]
result = statistics.mean(d)

print('result: ', result)
