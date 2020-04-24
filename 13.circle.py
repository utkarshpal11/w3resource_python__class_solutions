# Write a Python class named Circle constructed by a radius and
# two methods which will compute the area and the perimeter of a circle


class Circle:

    def __init__(self, r):
        self.radius = r

    def perimeter(self):
        return 2*3.14*self.radius

    def area(self):
        return 3.14*self.radius*self.radius


c = Circle(4)
print(c.perimeter())
print(c.area())


c = Circle(4)
print(c.perimeter())
print(c.area())

c = Circle(10)
print(c.perimeter())
print(c.area())

c = Circle(7.5)
print(c.perimeter())
print(c.area())