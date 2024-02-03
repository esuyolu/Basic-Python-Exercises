# Write a function called disp_last_lines that prints the last n lines of a file to the screen:
# The first parameter of the function specifies the path expression of the file and
# the second parameter specifies the number of lines.

def disp_last_lines(path, n):
    l = []
    with open(path, 'r') as f:
        for line in f:
            l.append(line)
            size = len(l)
        for i in range((size-n), size):
            print(l[i], end='')


disp_last_lines('test.txt', 3)
