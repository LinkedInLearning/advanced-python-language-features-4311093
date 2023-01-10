# Example file for Advanced Python: Language Features by Joe Marini
# Use lambdas as in-place functions


def celsisus_to_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_to_celsisus(temp):
    return (temp-32) * 5/9


ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]

# Use regular functions to convert temps
print(list(map(fahrenheit_to_celsisus, ftemps)))
print(list(map(celsisus_to_fahrenheit, ctemps)))

# Use lambdas to accomplish the same thing
print(list(map(lambda t: (t-32) * 5/9, ftemps)))
print(list(map(lambda t: (t * 9/5) + 32, ctemps)))
