import math as m
# I know this kinda looks stupid but it works
def determine(num):
    if num > m.pow(4, 4) and m.fmod(num, 34) == 4:
        return print("True")
    else:
        return print("False")

num = 922

determine(num)

num = 914

determine(num)

num = 854

determine(num)
determine(num)