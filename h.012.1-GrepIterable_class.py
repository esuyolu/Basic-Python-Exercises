# Write a iterable class called GrepIterable,
# which returns lines containing certain words in a file.
# In the __init__ method, the class will receive the path expression of the file and the text to be searched.
#
# def __init__(self, path, text):
#      pass
#
# The __next__ method of the iterator object will output the message as follows:
#
# <line number>: characters on line

class GrepIterable:
    def __init__(self, path, text):
        self.path = path
        self.text = text

    def __iter__(self):
        return GrepIterator(self.path, self.text)


class GrepIterator:
    def __init__(self, path, text):
        self.path = path
        self.text = text
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            list_file = list(file)
            size = len(list_file)

        if self.i >= size:
            raise StopIteration()

        self.i += 1

        if self.text in list_file[self.i - 1]:
            return f'<{self.i}>: {list_file[self.i - 1][:-1]}'
        else:
            return ''


for line in GrepIterable('text.txt', 'gül'):
    print(line)

