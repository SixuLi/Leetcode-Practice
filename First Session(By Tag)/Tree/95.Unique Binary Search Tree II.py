# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS
# When using i as root, the left subtree must contain nodes 1 to i-1 and right subtree contains nodes i+1 to n.

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right + 1):
            LeftTree = self.dfs(left, i - 1)
            RightTree = self.dfs(i + 1, right)
            for l in LeftTree:
                for r in RightTree:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res