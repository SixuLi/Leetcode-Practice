# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS
# In this problem, we need to iterate until the tree is None. And in each iteration, the leaves of the tree should be reduced.
# We do this by return None each time a leaf node is found during normal DFS. If its not a leaf node,
# just fetch the left and right subtree and return the node with the new left and right subtrees.

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        while root:
            leaves = []
            root = self.dfs(root, leaves)
            res.append(leaves)
        return res

    def dfs(self, root, leaves):
        if not root.left and not root.right:
            leaves.append(root.val)
            return None
        if root.left:
            left = self.dfs(root.left, leaves)
            root.left = left
        if root.right:
            right = self.dfs(root.right, leaves)
            root.right = right
        return root