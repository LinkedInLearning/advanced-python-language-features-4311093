# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class Person():
  def __init__(self):
    self.fname = "Joe"
    self.lname = "Marini"
    self.age = 25

  # use __repr__ to create a string useful for debugging
  def __repr__(self):
    return "<Person Class - fname:{0}, lname:{1}, age{2}>".format(self.fname, self.lname, self.age)

  # use str for a more human-readable string
  def __str__(self):
    return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

  # use bytes to convert the informal string to a bytes object
  def __bytes__(self):
    val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
    return bytes(val.encode('utf-8'))


# create a new Person object
cls1 = Person()

# use different Python functions to convert it to a string
print(repr(cls1))
print(str(cls1))
print("Formatted: {0}".format(cls1))
print(bytes(cls1))
