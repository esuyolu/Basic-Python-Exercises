class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_inside(self, x, y):
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return True

        return False

    def disp(self):
        print(f'x1 = {self.x1}, y1 = {self.y1}, x2 = {self.x2}, y2 = {self.y2}')

    def intersect(self, rect):
        self.x1 = max(self.x1, rect.x1)
        self.y1 = max(self.y1, rect.y1)
        self.x2 = min(self.x2, rect.x2)
        self.y2 = min(self.y2, rect.y2)

        if self.x1 >= self.x2 or self.y1 >= self.y2:
            return None
        else:
            return Rectangle(self.x1, self.y1, self.x2, self.y2)


r1 = Rectangle(10, 10, 20, 20)
r1.disp()

print('İçinde' if r1.is_inside(12, 14) else 'İçinde Değil')

r2 = Rectangle(15, 15, 30, 30)
r3 = r1.intersect(r2)
r3.disp()

