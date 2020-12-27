# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        