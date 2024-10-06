# Who is fibonacci bro💀
# Alright so first you need to make the function this is a function which takes a number as input and returns the nth number in the fibonacci sequence.
# First it checks if the input is less than or equal to 1 and if it is it prints an error messages and returns early
# Then it prints the first two numbers in the fibonacci sequence 0 and 1
# Then using a for loop from 2 to n it calculates the next number with the sum of the previous two numbers and calls it c
# Then it prints c and updates a and b to b and c respectively
# Finally it asks the user to enter a number and calls the function with that number as input.
def fib(n):
    if n <= 1:
        print("Invalid Input")
        return
    else:
        a = 0
        b = 1
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            if c >= n:
                break
            else:
                print(c)
                a = b
                b = c

fib(int(input("Enter a number: ")))

