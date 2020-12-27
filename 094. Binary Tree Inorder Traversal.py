# Given a binary tree, return the in-order traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time: O(N) because the recursion function T(N) = T(N/2) + 1
# space: O(N)

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        self.inorderTraversal_result = []
        self.inorderTraversal_dfs(root)
        return self.inorderTraversal_result

    def inorderTraversal_dfs(self, root):
        if root:
            if root.left:
                self.inorderTraversal_dfs(root.left)
            self.inorderTraversal_result.append(root.val)
            if root.right:
                self.inorderTraversal_dfs(root.right)

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    print(Solution().inorderTraversal(tree)) # [1, 3, 2]