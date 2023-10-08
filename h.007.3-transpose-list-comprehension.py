# Transpose a matrix with a single expression, using a list comprehension.
# For example:
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result:
# [[1, 4, 7], [2, 5, 9], [3, 6, 9]]

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result1 = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

print(result1)

result2 = [list(x) for x in zip(*a)]

print(result2)
