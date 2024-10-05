a = 10 # this is the global variable if there is no local variable a will be used.

def some_func():
    global a # this makes a global variable out of a local variable
    a = 15 # This local variable overrides the global variable
    b = 8
    print(a)
    print(b)

some_func()

print(a)