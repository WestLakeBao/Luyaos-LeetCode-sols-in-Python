class Solution(object):
    def findMaxAverage(self, nums, k):
        result = 0
        MAX = -float('inf')
        for i in range(len(nums)):
            result += nums[i]
            if i >= k - 1:
                if result > MAX:
                    MAX = result
                result -= nums[i + 1 - k]
        return MAX / k

print(Solution().findMaxAverage([1,12,-5,-6,50,3], k = 4)) # 12.75