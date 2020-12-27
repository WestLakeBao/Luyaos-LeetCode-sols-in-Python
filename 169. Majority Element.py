# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums)//2] # the default is b because b can always come from more elements than a come from
