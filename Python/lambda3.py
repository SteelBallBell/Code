from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda n: n % 2 == 0, nums)) # Filters the list and returns only the even numbers
doubled_evens = list(map(lambda n: n * 2, evens)) # Doubles the even numbers
sum = reduce(lambda a, b: a + b, doubled_evens)

print(evens)
print(doubled_evens)
print(sum)

# From what I can understand lambda is basically a shorter way of writing a function that is purpose made for one purpose
# In this case it filters and maps the list