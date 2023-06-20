# Read two texts from the keyboard. Whether these two texts are composed of exactly the same characters.
# Print in True/False format.
# For example, "ankara" and "karanak" consist of the same characters.

s1 = input('enter first text: ')
s2 = input('enter second text: ')

set_of_s1 = set(s1)
set_of_s2 = set(s2)

result = set_of_s1 == set_of_s2

print('Are the two texts made up of the same characters?', result)
