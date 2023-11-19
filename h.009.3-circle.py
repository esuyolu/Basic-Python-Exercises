import math


class Circle:
    def __init__(self, *, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def disp(self):
        print(f'center = ({self.x}, {self.y}), radius = {self.r}')

    def move(self, x_off, y_off):
        self.x += x_off
        self.y = y_off

    def is_inside(self, x, y):
        d = math.sqrt(math.pow(x - self.x, 2) + math.pow(y - self.y, 2))
        return d <= self.r


c = Circle(x=10, y=12, r=5)
c.disp()

c.move(-2, 4)
c.disp()

print('İçinde' if c.is_inside(5, 7) else 'İçinde Değil')
