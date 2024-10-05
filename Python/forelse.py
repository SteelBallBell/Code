nums = [10, 21, 18, 26, 21]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("No number found")