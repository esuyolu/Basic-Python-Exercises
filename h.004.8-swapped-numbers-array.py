# Create a list of two-digit int numbers.
# Then put the digits of the elements of this list in the swapped form.

a = [12, 56, 89, 32, 19, 99, 43]
b = []

for num in a:
    val = (num % 10) * 10 + (num // 10)
    b.append(val)

a = b

print(a)
