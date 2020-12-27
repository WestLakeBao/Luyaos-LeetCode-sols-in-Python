# Given an unsorted array of integers, find the length of longest increasing subsequence.

class Solution(object):
    def lengthOfLIS(self, nums):
        result = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    result[i] = max(result[i], result[j] + 1)
        return max(result) if result else 0