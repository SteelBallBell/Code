from typing import List

nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []

# This is probably even worse the better way of doing this is to use a dictionary
# This is O(n^2) time complexity

solution = Solution()
result = solution.twoSum(nums, target)
print(result)