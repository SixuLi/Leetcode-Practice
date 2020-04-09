# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Recursion.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Solution 2: DFS with Stack.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        maxdepth = 0
        while stack:
            node, depth = stack.pop()
            maxdepth = max(maxdepth, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return maxdepth

# Solution 3: BFS with Queue.

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        Q = [root]
        depth = 0
        while Q:
            depth += 1
            for i in range(len(Q)):
                p = Q.pop(0)
                if p.left:
                    Q.append(p.left)
                if p.right:
                    Q.append(p.right)
        return depth