class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == 2:
            return 1
        else:
            for i in range(x):
                if i * i == x:
                    return i
                elif i * i > x:
                    return i - 1
            
print(Solution().mySqrt(4))

# This is stupid time complexity but it works