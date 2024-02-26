'''Define a class named Shape and its subclass Square. The Square
class has an init function which takes length as argument. Both
classes have an area function which can print the area of the
shape where Shape’s area is 0 by default'''


class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2

shape = Shape()
print("Area of generic shape:", shape.area())

square = Square(5)
print("Area of square:", square.area())