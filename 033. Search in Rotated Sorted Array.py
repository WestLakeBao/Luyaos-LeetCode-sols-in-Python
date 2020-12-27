# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# If found in the array return its index, otherwise return -1

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# time: O(logN)
# space: O(1)

class Solution(object):
    def search(self, nums, target):
        # solution 1: 72%
        def minIndex():
            if nums[0] < nums[-1]:
                return 0
            left, right = 0, len(nums)-1
            while (right-left) > 1:
                mid = (left+right)//2
                if nums[mid] < nums[right]:
                    right = mid
                elif nums[mid] > nums[left]:
                    left = mid
            return max(left, right)

        def binarySearch(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1

        if not nums: return -1
        left, right = 0, len(nums)-1
        min_index = minIndex()
        if target >= nums[min_index] and target <= nums[right]: # when to search in the left part to min_index
            return binarySearch(min_index, right)
        elif target >= nums[min_index] and target >= nums[left]: # when to search in the right part to min_index
            return binarySearch(left, min_index)
        return -1 # when nums[right] < target < nums[left]

if __name__ == '__main__':
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1