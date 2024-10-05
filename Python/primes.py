import math
nums = int(input("Enter a number you want to check if its prime: "))

for i in range(2, nums):
    if nums % i == 0:
        print("Not prime")
        break
else:
        print("Prime")
