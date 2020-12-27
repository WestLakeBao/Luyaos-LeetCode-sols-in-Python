# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        self.max_depth = 1
        self.maxDepth_dfs(root, 1)
        return self.max_depth

    def maxDepth_dfs(self, root, depth):
        if not root.left and not root.right:
            self.max_depth = max(self.max_depth, depth)
        if root.left:
            self.maxDepth_dfs(root.left, depth + 1)
        if root.right:
            self.maxDepth_dfs(root.right, depth + 1)

if __name__ == '__main__':
    tree3 = TreeNode(3)
    tree3.left = TreeNode(9)
    tree3.right = TreeNode(20)
    tree3.right.left = TreeNode(15)
    tree3.right.right = TreeNode(7)
    print(Solution().maxDepth(tree3))  # 3