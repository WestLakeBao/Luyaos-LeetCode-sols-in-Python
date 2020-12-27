# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]

class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())
        return nums

print(Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3)) # [5, 6, 7, 1, 2, 3, 4]