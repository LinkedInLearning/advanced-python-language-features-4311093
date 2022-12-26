# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

x = None

# Literal patterns are explicit values like integers, strings, Booleans, etc
match x:
    case 0:
        print("Zero")
    case "Zero":
        print(0)
    case None:
        print("Nothing")
    case _:
        print("No match")
