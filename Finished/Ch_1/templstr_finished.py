# Example file for Advanced Python: Language Features by Joe Marini
# demonstrate template string functions

from string import Template


# Usual string formatting with format()
str1 = "Advanced Python: Language Features"
str2 = "Joe Marini"
outputstr = f"You're watching {str1} by {str2}"
print(outputstr)

# create a template with placeholders
templ = Template("You're watching ${title} by ${author}")

# use the substitute method with keyword arguments
str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
print(str2)

# use the substitute method with a dictionary
data = {
    "author": "Joe Marini",
    "title": "Advanced Python"
}
str3 = templ.substitute(data)
print(str3)
