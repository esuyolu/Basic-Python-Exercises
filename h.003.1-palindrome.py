# Print as True/False whether the elements of the two lists a and b are palindrome.
# a = [10, 'ali', 'veli', 20, 'selami']
# b = ['selami', 20, 'veli', 'ali', 10]
#
# Since these two lists are palindrome, the text True should appear on the screen.

a = [10, 'ali', 'veli', 20, 'selami']
b = ['selami', 20, 'veli', 'ali', 10]

reverse_of_b = b[::-1]

result = a == reverse_of_b

print('Are a and b palindrome ? ', result)
