# Create a list. Replace the first half of the list with the second half and print the list on the screen.

# Let a list be like the following:
# a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# list a should become:
#
# [60, 70, 80, 90, 100, 10, 20, 30, 40, 50]

# The list can have an odd number of elements.
# In this case, the middle element should not be affected by the change.

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

mid = len(a) // 2

temp = a[:(mid + len(a) % 2)]
a[:(mid + len(a) % 2)] = a[(mid + len(a) % 2):]
a[(mid + len(a) % 2):] = temp

print(a)
# [60, 70, 80, 90, 100, 10, 20, 30, 40, 50]

# If the list has an odd number of items

b = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

size = len(b)
mid = size // 2

temp = b[:mid]
b[:mid] = b[(mid + size % 2):]
b[(mid + size % 2):] = temp

print(b)
# [70, 80, 90, 100, 110, 60, 10, 20, 30, 40, 50]
