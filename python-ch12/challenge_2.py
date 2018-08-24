import math
class Circle():
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        return self.redius ** 2 *  math.pi


a_circle = Circle(1)
print(a_circle.area())
b_circle = Circle(5)
print(b_circle.area())
