# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

x = 0

# Literal patterns are explicit values like integers, strings, Booleans, etc
match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case "Zero":
        print(0)
    case None:
        print("Nothing")
    case _:
        print("No match")
