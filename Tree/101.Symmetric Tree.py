# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion
# For given two sibling nodes l and r, we need to check whether l.left == r.right and l.right == r.left.

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        return self.dfs(l.left, r.right) and self.dfs(l.right, r.left)

# Solution 2: Iteration
# Change the above recursion into iteration.

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        queue = [(root.left, root.right)]
        while queue:
            p, q = queue.pop(0)
            if not check(p,q):
                return False
            if p:
                queue.append((p.left, q.right))
                queue.append((p.right, q.left))
        return True