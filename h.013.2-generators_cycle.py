# The standard function called cycle in the itertools module takes a iterable object from us
# and gives us a iterator object. When this object is iterated, the elements in the iterable object
# that we give to it are given in a cyclical manner indefinitely.
# Write this function both as a iterable class and as a generator function.
# You can test it with the following code:
#
# a = ['A', 'B', 'C']
# for index, x in enumerate(mycycle(a)):
#      if index == 100:
#          break
#      print(x, end=' ')

# by generator function

def mycycle(iterable):
    result = []
    while True:
        for i in range(len(iterable)):
            result.append(iterable[i])
            yield result


# test by generator function

a = ['A', 'B', 'C']
for index, x in enumerate(mycycle(a)):
    if index == 100:
        break
    print(index, x)

print('****************************************************************************************************')


# by iterator class

class MyCycleIterable:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.iterable = iterable

    def __iter__(self):
        return MyCycleIterator(self.iterable)


class MyCycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.i = 0
        self.result = []

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while True:
                self.result.append(self.iterable[self.i])
                self.i += 1
                if self.i == len(self.iterable):
                    self.i = 0
                return self.result
        except StopIteration:
            pass


# test by iterator class

iterator = MyCycleIterable(['A', 'B', 'C'])

for index, x in enumerate(iterator):
    if index == 100:
        break
    print(index, x)
