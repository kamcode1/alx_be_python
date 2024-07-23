import math


class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.lenght = length
        self.width = width
    def area(self):
        return self.lenght * self.width

class Circle(Shape):
    from math import pi
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        area = math.pi * (self.radius ** 2)
        return area
    

        