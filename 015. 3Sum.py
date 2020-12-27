# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Example
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# time: O(N^2)
# space: O(N^2)

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        if len(nums) >= 3 and nums[0] == 0 and nums[- 1] == 0:
            return [[0, 0, 0]]

        result = set()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:  ####### skip duplicates#######
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  ####### skip duplicates#######
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  ####### skip duplicates#######
                        right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return [list(r) for r in result]

if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
    print(Solution().threeSum([1, 2, -2, -1])) # []