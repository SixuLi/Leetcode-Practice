# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1:

# Time Complexity: O(N)
# Space Complexity: O(H), where H is the tree height.

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.ms(root)
        return self.res

    def ms(self, root):
        if not root:
            return 0
        l = max(0, self.ms(root.left))
        r = max(0, self.ms(root.right))
        self.res = max(self.res, root.val + l + r)
        return root.val + max(l, r)