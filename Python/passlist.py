# Make function that takes list from the user as input and returns the number of even and odd numbers in the list

def count(numbers):
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

numbers = []
n = int(input("Enter the length of the list: "))
for i in range(n):
    ele = int(input())
    numbers.append(ele)

even, odd = count(numbers)
print(even, odd)

# to pass a list into a function you have to use for loop to put the elements of the list in the function