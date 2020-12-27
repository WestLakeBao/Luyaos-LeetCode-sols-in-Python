# Given a sorted array nums, remove the duplicates ***in-place*** such that each element appear only once and return the new length.
## the sorted array can contain 0

# time: O(N)
# space:

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2])) # 2