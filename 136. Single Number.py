# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num
        return result