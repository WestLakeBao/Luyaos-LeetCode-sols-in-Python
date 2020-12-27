# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j, end = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[end] = nums2[j]
                j -= 1
            else:
                nums1[end] = nums1[i]
                i -= 1
            end -= 1
        if i < 0:  # nums2 has elements left
            nums1[:j + 1] = nums2[:j + 1]
        return nums1

if __name__ == '__main__':
    print(Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))  # [1,2,2,3,5,6]