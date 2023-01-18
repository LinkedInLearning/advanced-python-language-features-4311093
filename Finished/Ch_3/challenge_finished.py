# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# get the total length of the string
l = len(test_str)

# count the number characters
nums = len([c for c in test_str if c.isnumeric()])

# count the punctuation characters
punct = len([c for c in test_str if c in string.punctuation])

# use a set to count the unique letters
unique = "".join({c for c in test_str if c.isalpha()})

# print the data
str_data = {
    "Length:": l,
    "Digits:": nums,
    "Punctuation": punct,
    "Unique Letters": unique,
    "Unique Count": len(unique)
}
pprint.pp(str_data)
