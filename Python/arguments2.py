# def sum(a, *b):
#    c = a + b
#    print(c)
#    print(b)
#
#sum(24,21,20,18)

# this does not work because it is not a tuple

def sum(*b):

    c = 0

    for i in b:
        c = c + i

    print(c)
    print(b)

sum(24, 21, 20, 18)

# this works because it adds all the numbers in the tuple into a variable called c and prints it along with the tuple