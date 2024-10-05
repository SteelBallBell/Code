# The function shown here is a formal argument.
def add(a,b):
    c = a + b
    print(c)

# The function shown here is an actual argument.
add(5, 4)
# the types of actual arguments are position keyword default and variable length

# if you do not know the sequence of the arguments, you can use specific
# keywords like a=5, b=4

def person(name, age=18):
    print(name)
    print(age)

person("John") # this works because the default value for age is 18
person("John", 25) # this will override the default value