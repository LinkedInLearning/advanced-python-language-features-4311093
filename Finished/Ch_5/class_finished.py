# Example file for Advanced Python: Language Features by Joe Marini
# Objects pattern matching example - matches against object types

# define some geometric shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return 3.14 * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def getarea(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height


# create a list of some shapes
shapes = [Circle(5), Square(4), Rectangle(4, 6),
          Square(7), Circle(9), Rectangle(2, 5)]

# use pattern matching to process each shape
for shape in shapes:
    match shape:
        case Circle():
            print(f"Circle with area {shape.getarea()}")
        case Square():
            print(f"Square with area {shape.getarea()}")
        case Rectangle():
            print(f"Rectangle with area {shape.getarea()}")
        case _:
            print(f"Unrecognized shape: {type(shape)}")
