# Create a list. Replace the first half of the list with the second half and print the list on the screen.

# Let a list be like the following:
# a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# list a should become:
#
# [60, 70, 80, 90, 100, 10, 20, 30, 40, 50]

# The list can have an odd number of elements.
# In this case, the middle element should not be affected by the change.

# If the list has an even number of items

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

size = len(a) // 2

b = a[0:size]
c = a[size:]

a = c + b
print(a)

# If the list has an odd number of items

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

size = len(a) // 2

b = a[0:size]
c = a[size+1:]
a[0:size] = c
a[size+1:] = b

print(a)
