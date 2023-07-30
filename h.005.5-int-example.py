# Write a function called digitate that takes a iterable object of int values as a parameter
# and returns a tuple array by obtaining a tuple from the digits in that list:
#
# vals = [23, 4, 765, 34589, 42]
# result = digitate(vals)
# print(result)
#
# # [(2, 3),(4, ), (7, 6, 5), (3, 4, 5, 8, 9), (4, 2)]

def digitate(l):
    result = list()
    for i in l:
        x = list()
        while i:
            x.append(i % 10)
            i //= 10
        t = tuple(x[::-1])
        result.append(t)

    return result


# Control
vals = []

while (a := int(input('Enter a number: '))) != 0:
    vals.append(a)


result = digitate(vals)
print(result)

