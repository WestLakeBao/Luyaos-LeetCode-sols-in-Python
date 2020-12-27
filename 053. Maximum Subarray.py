# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        import sys
        if len(nums) == 1:
            return nums[0]
        max_sum = 0 - sys.maxsize
        sum = 0 - sys.maxsize
        for num in nums:
            if num > num + sum:
                sum = num
            else:
                sum += num
            if sum > max_sum:
                max_sum = sum
        return max_sum

if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6