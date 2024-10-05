a = 10
print(id(a))

"""
 This function prints the id of the global variable 'a',
 assigns the value of the global variable 'a' to 'x',
 prints the value of 'a' and 'x', and then changes the value of 'a' to 15.
"""

def some_func():
    
   
    a = 9
    x = globals()["a"]
    print(id(x))
    print(a)
    print(x)

    globals ()["a"] = 15

some_func() 