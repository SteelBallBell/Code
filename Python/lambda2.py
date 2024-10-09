def is_even(n):
    return n % 2 == 0 # If the number is even it returns true

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(is_even, nums)) # Filters the list and returns only the even numbers

print(evens)