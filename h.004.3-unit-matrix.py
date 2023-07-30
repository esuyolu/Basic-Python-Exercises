# Read an n value of type int from the keyboard.
# Construct an n x n square unit matrix in list format.
# Print this list you created using two nested loops.

n = int(input('enter an int value: '))

result = []

for i in range(n):
    row = [0] * n
    row[i] = 1
    result.append(row)

for i in result:
    for j in i:
        print(j, end=' ')
    print()


