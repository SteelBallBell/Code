# Finally Multi-Dimensional Arrays
from numpy import *

arr1 = array([
    [1, 2, 3, 4],
    [7, 8, 9, 10],
])

arr2 = arr1.flatten()
print(arr2)
# Flattens Arrays
print()
arr3 = arr1.reshape(2, 2, 2)
print(arr3)
print()
# Makes the array 3x2x2

# mat = matrix(arr1)
# print(mat)

m1 = matrix('1 2 3; 4 7 8; 9 10 11')
print(m1)

print()

m2 = m1 + m1
print(m2)

# you also have m.max() and m.min() functions when dealing with matrices
    