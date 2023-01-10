# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


# define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg

    return result


# pass different arguments
print(addition(5, 10, 15, 20))
print(addition(1, 2, 3))

# pass an existing list
myNums = [5, 10, 15, 20]
print(addition(*myNums))
