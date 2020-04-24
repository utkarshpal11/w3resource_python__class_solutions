# Write a Python class named Rectangle constructed by a length and width
# and a method which will compute the area of a rectangle.


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return print('area: ', area)


area = Rectangle(5, 8)
area.area() 