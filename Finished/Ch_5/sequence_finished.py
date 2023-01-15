# Example file for Advanced Python: Language Features by Joe Marini
# Sequence pattern matching example - matches against value sequences

import math


operations = [
    ["Add", 1, 2, 3, 4],
    ["Mul", 5, 6],
    ["Add", 10, 20],
    ["Sqrt", 9],
]

result = 0

for op in operations:
    match op:
        case "Add", *nums:
            result = sum(nums)
        case "Mul", num1, num2:
            result = num1 * num2
        case "Sqrt", num:
            result = math.sqrt(num)
        case _:
            continue

    print(f"{op}: {result}")
