# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        def constructTree(nums, start, end):
            if start > end:
                return
            mid = int((start + end)/2)
            node = TreeNode(nums[mid])

            if start == end:
                return node

            node.left = constructTree(nums, start, mid - 1)
            node.right = constructTree(nums, mid + 1, end)
            return node

        return constructTree(nums, 0, len(nums) - 1)
    

if __name__ == '__main__':
    print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))