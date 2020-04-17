# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Binary Search
# Time Complexity: O(logN)
# Space Complexity: O(1)

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        distance = float('inf')
        while root:
            if distance > abs(target - root.val):
                distance = abs(target - root.val)
                res = root.val
            if target == root.val:
                return root.val
            elif target > root.val:
                root = root.right
            else:
                root = root.left
        return res

