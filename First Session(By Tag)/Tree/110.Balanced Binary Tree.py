# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion
# The two conditions that we need to check for a height-balanced binary tree are:
# 1. Left subtree and right subtree are balanced.
# 2. |max_left_height - max_right_height| <= 1

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return (self.isBalanced(root.left) and self.isBalanced(root.right) and abs(
            self.MaxDepth(root.left) - self.MaxDepth(root.right)) <= 1)

    def MaxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.MaxDepth(root.left), self.MaxDepth(root.right))
