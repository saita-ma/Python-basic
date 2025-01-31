class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __clone(self):
        return Rectangle(self.width, self.height)

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        else:
            return False

    def __iadd__(self, other):
        if isinstance(other, Rectangle):
            s = self.get_square() + other.get_square()
            self.width = 1
            self.height = s
            return self

    def __add__(self, other):
        return self.__clone().__iadd__(other)

    def __isub__(self, other):
        if isinstance(other, Rectangle):
            s = self.get_square() - other.get_square()
            if s > 0:
                self.width = 1
                self.height = s
            else:
                raise ValueError("First rectangle smaller then second")
            return self

    def __sub__(self, other):
        return self.__clone().__isub__(other)

    def __imul__(self, n):
        s = self.get_square() * n
        self.width = 1
        self.height = s
        return self

    def __mul__(self, n):
        return self.__clone().__imul__(n)

    def __itruediv__(self, n):
        s = self.get_square() / n
        self.width = 1
        self.height = s
        return self

    def __truediv__(self, n):
        return self.__clone().__itruediv__(n)

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2

assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
