# Write a class named LastLinesIterable that returns the last n lines of a file
# from beginning to end.
# The __init__ method of the class takes the path of the file and
# the number of lines from the end as parameters.
# The class should output one row at each iteration:
#
# def __init__(self, path, n):
#      pass
#
# An example usage might be:
#
# for line in LastLinesIterable('test.txt', 10):
#      print(line)

class LastLinesIterable:
    def __init__(self, path, n):
        self.path = path
        self.n = n

    def __iter__(self):
        return LastLinesIterator(self.path, self.n)


class LastLinesIterator:
    def __init__(self, path, n):
        self.path = path
        self.n = n
        self.i = self.n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= 0:
            raise StopIteration()

        self.i -= 1

        with open(self.path, 'r', encoding='utf-8') as file:
            list_file = list(file)
            size = len(list_file)

        return list_file[size - self.i - 1][:-1]


for line in LastLinesIterable('text.txt', 2):
    print(line)
