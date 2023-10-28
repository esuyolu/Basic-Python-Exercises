import itertools

d_values = {
    'A': {'B': 5, 'C': 7, 'D': 10},
    'B': {'A': 5, 'D': 4, 'E': 17, 'G': 20},
    'C': {'A': 7, 'D': 6, 'F': 9},
    'D': {'A': 10, 'B': 4, 'C': 6, 'E': 3, 'F': 12},
    'E': {'B': 17, 'D': 3, 'F': 14, 'G': 6},
    'F': {'C': 9, 'D': 12, 'E': 14, 'G': 10},
    'G': {'B': 20, 'E': 6, 'F': 10}
}

d = {
    'A': 'BCD',
    'B': 'ADEG',
    'C': 'ADF',
    'D': 'ABCEF',
    'E': 'BDFG',
    'F': 'CDEG',
    'G': 'BEF'
}

cities = ['B', 'C', 'D', 'E', 'F', 'G']
min_distance = 0
way = ''
min_distances_ways = {}
ways = []
wrong_ways = []
common = []
temp_ways = []

for per_cities in list(itertools.permutations(cities)):
    ways.append(''.join(per_cities))

for way in ways:
    for i in range(5):
        if way[i + 1] not in d[way[i]]:
            wrong_ways.append(way)

wrong_ways = list(set(ways) & set(wrong_ways))
ways = list(set(ways) - set(wrong_ways))

wrong_ways = []

for way in ways:
    if way[0] in 'EFG':
        wrong_ways.append(way)

for way in ways:
    if way[5] not in 'BCD':
        wrong_ways.append(way)

ways = list(set(ways) - set(wrong_ways))

temp_ways = []

for way in ways:
    temp_ways.append('A' + way + 'A')


for way in temp_ways:
    min_distance = 0
    for i in range(7):
        c1 = way[i]
        c2 = way[i + 1]
        min_distance += d_values[c1][c2]

    min_distances_ways[way] = min_distance

min_distance = min(min_distances_ways.values())

for k, v in min_distances_ways.items():
    if min_distance == v:
        way = k

print('way:', way, 'minimum distance:', min_distance)
