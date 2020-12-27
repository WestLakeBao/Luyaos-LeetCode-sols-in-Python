# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one duplicate number in nums, return this duplicate number.

class Solution(object):
    def findDuplicate(self, nums):
        slow = fast = head = len(nums)
        slow = nums[slow - 1]
        fast = nums[nums[fast - 1] - 1]
        while slow != fast:
            slow = nums[slow - 1]
            fast = nums[nums[fast - 1] - 1]
        while head != slow:
            head = nums[head - 1]
            slow = nums[slow - 1]
        return head