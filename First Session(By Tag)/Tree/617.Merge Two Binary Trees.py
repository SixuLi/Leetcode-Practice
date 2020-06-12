# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion(Merge two trees on the original tree)

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# Solution 2: Recursion(Merge two trees with a new created tree)

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if t1 and t2:
            tree_merge = TreeNode(t1.val+t2.val)
            tree_merge.left = self.mergeTrees(t1.left, t2.left)
            tree_merge.right = self.mergeTrees(t1.right, t2.right)
        elif t1 and not t2:
            tree_merge = TreeNode(t1.val)
            tree_merge.left = self.mergeTrees(t1.left, None)
            tree_merge.right = self.mergeTrees(t1.right, None)
        elif not t1 and t2:
            tree_merge = TreeNode(t2.val)
            tree_merge.left = self.mergeTrees(None, t2.left)
            tree_merge.right = self.mergeTrees(None, t2.right)
        return tree_merge