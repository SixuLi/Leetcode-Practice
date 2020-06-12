# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Recursion
# In this question, the main problem is to find every left leaf nodes.
# Besides decide whether it is a leaf, we can use a signal to distinguish whether the leaf is a left child.

# Time Complexity: O(N)
# Space Complexity: O(H) where H is the tree height.

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = self.dfs(root, 1)
        return res

    def dfs(self, root, sign):
        if not root.left and not root.right and sign == 0:
            return root.val
        total = 0
        if root.left:
            total += self.dfs(root.left, 0)
        if root.right:
            total += self.dfs(root.right, 1)
        return total

# Solution 2: DFS with Iteration
# Just change the Recursion into Iteration.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            node, sign = stack.pop()
            if self.is_leaf(node) and sign == 0:
                res += node.val
            if node.left:
                stack.append((node.left, 0))
            if node.right:
                stack.append((node.right, 1))
        return res