from numpy import *

arr = array([1, 2, 3, 4, 5])

# this is what i thought was the correct way to do it
for e in arr:
    e = e + 5
    print(e)

# correct way to do it is
arr = arr + 5
print(arr)
