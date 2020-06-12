# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Recursion
# Use the same check conditions in Problem 112. The only difference here is that we need to save the path during DFS.

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, res, [])
        return res

    def dfs(self, root, sum, res, cur):
        if not root:
            return
        if root.val == sum and not root.left and not root.right:
            res.append(cur + [root.val])
            return
        self.dfs(root.left, sum - root.val, res, cur + [root.val])
        self.dfs(root.right, sum - root.val, res, cur + [root.val])