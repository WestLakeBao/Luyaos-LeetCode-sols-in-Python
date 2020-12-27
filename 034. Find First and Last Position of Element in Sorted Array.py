# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# If the target is not found in the array, return [-1, -1].

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# time: O(logN)
# space:

class Solution(object):
    def searchRange(self, nums, target): # nums is sorted in ascending order
        from bisect import bisect_left
        # solution 1: using binary search library, beats 96%
        left, right = 0, len(nums)-1
        result = [-1, -1]
        bs = bisect_left(nums, target) #  If x is already present in a, the insertion point will be before (to the left of) any existing entries.
        if not nums or bs >= len(nums) or nums[bs] != target:
            return [-1, -1]
        mid = (left+right)//2
        while nums[mid] != target:
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)//2
        i = mid
        while i >= 0 and nums[i] == target:
            i -= 1
        result[0] = i+1
        i = mid
        while i< len(nums) and nums[i] == target:
            i += 1
        result[1] = i-1
        return result

if __name__ == '__main__':
    print(Solution().searchRange(nums=[2, 2], target=3))  # [-1,-1]
    print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4]
    print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1, -1]
    print(Solution().searchRange([1, 3], 1))  # [0,0]