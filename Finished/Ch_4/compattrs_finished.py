# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"
        else:
            raise AttributeError(f"{attr} is not a valid attribute")

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return ("rgbolor", "hexcolor")


# create an instance of myColor
cls1 = MyColor()
# print the value of a computed attribute
print(cls1.rgbcolor)
print(cls1.hexcolor)

# set the value of a computed attribute
cls1.rgbcolor = (125, 200, 86)
print(cls1.rgbcolor)
print(cls1.hexcolor)

# access a regular attribute
print(cls1.red)

# list the available attributes
print(dir(cls1))
