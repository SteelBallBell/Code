def fact(n):
    if n < 0:
        return print("Factorial does not exist for negative numbers")
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter the number: "))
result = fact(n)
print(result)