# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Recursion
# We use DFS to store every root-to-leaf path and do the calculation for each path and sum them up.

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, res, [])
        count = 0
        for List in res:
            cur_count = 0
            for i in range(len(List) - 1):
                cur_count = (cur_count + List[i]) * 10
            cur_count += List[-1]
            count += cur_count
        return count

    def dfs(self, root, res, cur):
        if not root:
            return
        if not root.left and not root.right:
            res.append(cur + [root.val])
            return
        self.dfs(root.left, res, cur + [root.val])
        self.dfs(root.right, res, cur + [root.val])

# Solution 2: DFS
# An improvement version of Solution 1. Here, instead of store each root-to-leaf path, we do the summation during the DFS.

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, cur):
        if not root:
            return
        if not root.left and not root.right:
            cur += root.val
            self.res += cur
            return
        self.dfs(root.left, (cur + root.val) * 10)
        self.dfs(root.right, (cur + root.val) * 10)