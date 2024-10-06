x = 5 # Ok so this is the number you want to find the factorial of
def fact(x): # This is the function with (x) as a parameter

    f = 1 # This is the result of the factorial operation on x

    if x <= 0:
        print("Invalid Input")
        return
    else:
        for i in range(1, x+1):
            f = f * i

        return f
            
result = fact(x)
print(result)