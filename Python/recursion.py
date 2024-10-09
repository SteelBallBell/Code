import sys # This is to set the recursion limit
import math # This was imported to see if I could set the recursion limit to infinity but it didn't work because i got an error about floats

sys.setrecursionlimit(100000) # So I just set it to 100000 because it was pretty high and it wasnt giving me an error

counter = 0 # This is a global variable that will be used in the function to count how many times it has been called
def greet():
    global counter # This makes the global variable 'counter' available to the function
    counter += 1
    print("Hello" + str(counter)) # This adds one to the global variable 'counter' each time its called
    greet() # This calls the function again inside itself this is called recursion


greet() # This calls the function to start the recursion
print(counter) # This line is useless but it prints the number of times the function has been called.