from array import *

vals = array('i', [5, 9, 8, 4, 2])
print(vals)

print(vals.buffer_info)
print(vals.typecode)
vals.reverse()
print(vals)

for i in vals:
    print(i)

# for i in range(5):
#    print(vals[i])
# another possible way

NewArray = array(vals.typecode, (a for a in vals))
# This is how to copy an array to another array

SquaredArray = array(vals.typecode, (a*a for a in vals))
# this is how to square an array    