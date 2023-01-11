# Example file for Advanced Python: Language Features by Joe Marini
# Python coding style example file

# imports go on their own lines
import datetime
import platform


# two blank lines separate classes from other functions
class MyClass():
    def __init__(self):
        self.prop1 = "my class"
        self.now = datetime.datetime.now

    # within classes, one blank line separates methods
    def function_name(self, use_name):
        print(platform.version())
        if use_name:
            print(platform.uname())


# Long comments, like this one that flow across several lines, are
# limited to 72 characters instead of 79 for lines of code.
cls1 = MyClass()
cls1.prop1 = "hello world"
cls1.function_name(True)
