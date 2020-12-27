# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (left.val == right.val) and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)