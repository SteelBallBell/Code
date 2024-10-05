from numpy import *

arr = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next the next value of the array: "))
    arr.append(x)

print(arr)

val = int(input("Enter the value you want to search: "))

k = 0
for e in arr:
    if e==val:
        print(k+1)
        break
    
    k = k+1

print(array)