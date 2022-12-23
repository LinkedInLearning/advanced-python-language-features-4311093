# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


def myFunction(arg1, arg2=None):
  """myFunction(arg1, arg2=None) --> Doesn't really do anything special.

  Parameters:
  arg1: the first argument. Whatever you feel like passing.
  arg2: the second argument. Defaults to None. Whatever makes you happy.
  """
  print(arg1, arg2)


print(myFunction.__doc__)
