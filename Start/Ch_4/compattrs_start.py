# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        else:
            raise AttributeError(f"{attr} is not a valid attribute")

    # TODO: use setattr to dynamically return a value
    # def __setattr__(self, attr, val):
    #     pass

    # TODO: use dir to list the available properties
    # def __dir__(self):
    #     pass


# create an instance of myColor
cls1 = MyColor()
# TODO: print the value of a computed attribute
print(cls1.rgbcolor)

# TODO: set the value of a computed attribute

# TODO: access a regular attribute

# TODO: list the available attributes
