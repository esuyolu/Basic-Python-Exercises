# Create a tuple list from the numbers in a list with a list comprehension.
# The first element of the tuple must consist of the number itself,
# and the second element must consist of the words "odd" or "even". For example:
#
# a = [1, 2, 3, 4, 5]
# [(1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd')]

a = [1, 2, 3, 4, 5]
b = {0: 'even', 1: 'odd'}

result = [(i, b.get(j)) for i in a for j in b.keys() if i % 2 == j]

print(result)
