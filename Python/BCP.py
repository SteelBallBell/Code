# Break Continue and Pass

av = 5

x = int(input("How many candies do you want?: "))

i = 1

while i <= x:
    print("Candy")
    i = i + 1
    av = av - 1
    if av == 0:
        print("Out of Stock")
        break
    
# in this the value for i is 1 and as long as i is less than or equal to x it will print "Candy"
# once i is greater than or equal to x the loop will end