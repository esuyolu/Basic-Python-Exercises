# Write a function named consecutive_total that returns a tuple to the largest sum of n adjacent numbers
# in a list and the starting index of that array.
#
# def consecutive_total(a, n):
#      pass
#
# The first parameter of the function specifies the list in question,
# and the second parameter specifies the amount of sequentiality.
# For example, in the list [3, 8, 6, 9, 4, 7, 5], the sequentiality is 2.
# In this case, the highest 2 side-by-side sum is 6 + 9 = 15.
# The value 6 is at index 2 of the list.
# In this case the function should return a tuple of the form (15, 2).
# If there are no elements in the list for n side by side, stop at that point.
# If there is more than one case where the adjacent sums are the largest,
# the higher order in the list should be returned.
from operator import itemgetter


def consecutive_total(a, n):
    temp_list = []
    for i in range(len(a)):
        if i + n >= len(a):
            break

        temp_sum = sum(a[i: i + n])
        temp_list.append((temp_sum, i))

    my_result = max(temp_list, key=itemgetter(0))
    return my_result


print(consecutive_total([3, 8, 6, 9, 4, 7, 5], 2))
