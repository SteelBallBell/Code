numbers = [12, 35, 1, 10, 34, 1]

def sort(numbers):
    print(sorted(numbers, reverse=True)[1])

sort(numbers)

# Solved easily with the help of the sorted function
# This simply sorts the list in descending order
# and returns the second largest element