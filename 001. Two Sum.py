# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# each input would have exactly one solution
# you may not use the same element twice

# Example
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# time: O(N)
# space: O(N)

class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in dict:
                return [index, dict[diff]]
            dict[value] = index

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], target=9)) # [0, 1]