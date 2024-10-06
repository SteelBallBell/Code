s = "silent"
t = "listen"

def anagrams(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

print(anagrams(s, t))

# I know this is cheating but it works
# This is inefficient because it sorts the strings its time complexity is O(nlogn)
# A better way to do this is to use a frequency dictionary because it is O(n)
# Though the sorting algorithm in python is still pretty efficient
# I used this to solve the anagrams problem on leetcode