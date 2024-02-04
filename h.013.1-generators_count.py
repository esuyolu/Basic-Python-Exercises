# The count function, found in the module called itertools in the Python standard library,
# gives us an iterator object. When this object is navigated,
# values are obtained with step increments starting from the start value and infinite.
# The parametric structure of the function is as follows:
#
# count(start = 0, step = 1)
#
# The count function in the standard library is written in the form of a iterator class.
# However, you should write this function both as a iterator class and as a generator function.
# You can test it with code like this:
#
# iterator = mycount(10, 2)
#
# for index, x in enumerate(iterator):
#      if index == 100:
#          break
#      print(x, end=' ')

# by generator function

def mycount(start=0, step=1):
    val = start
    while True:
        yield val
        val += step


# test by generator function

iterator = mycount(10, 2)

for index, x in enumerate(iterator):
    if index == 100:
        break
    print(index, x)

print('******************************')


# by iterator class
class MyCountIterable:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step

    def __iter__(self):
        return MyCountIterator(self.start, self.step)


class MyCountIterator:
    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.val = start - step

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.val += self.step
            return self.val
        except StopIteration:
            pass


# test by iterator class

iterator = MyCountIterable(10, 2)

for index, x in enumerate(iterator):
    if index == 100:
        break
    print(index, x)
