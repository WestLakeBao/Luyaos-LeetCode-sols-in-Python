# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

class Solution(object):
    def missingNumber(self, nums):
        i = 0
        while i <= len(nums) - 1:
            j = nums[i]  # idealy, i == nums[i] (e.g. 0 at position 0, 1 at position 1, 2 at position 2, and so on...)
            if i < len(nums) and j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1