# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.kthSmallest_dfs(root)
        return self.result

    def kthSmallest_dfs(self, root):
        if root:
            self.kthSmallest_dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.result = root.val
                return
            self.kthSmallest_dfs(root.right)