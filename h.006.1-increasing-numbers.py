# Write a function named increasing_numbers that creates an integer in ascending order
# from the characters in the text it receives with its parameter and returns it in the form of a list.

# The function should get the next value with the least number of characters greater than the previous value.
# Below are sample numbers entered as parameters and lists that the function should return:

# '0'												[0]
# '045349'										[0, 4, 5, 34]
# '77777777'									[7, 77, 777]
# '19510899'									[1, 9, 51, 89]
# '3141592653589793238462643'		[3, 14, 15, 92, 653, 5897, 9323, 84626]

def increasing_numbers(s):
    result = []
    i = 0
    k = 1

    if len(s) == 1:
        result.append(int(s))

    while k < len(s):
        value = int(s[i:k])
        result.append(value)

        i = k
        k += 1

        value = int(s[i:k])
        last_element = result[-1]

        while value <= last_element:
            if k >= len(s):
                break
            k += 1
            value = int(s[i:k])

    return result


n = input('enter a int type numeric text: ')
print(increasing_numbers(n))
