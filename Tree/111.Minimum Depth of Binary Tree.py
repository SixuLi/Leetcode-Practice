# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: BFS with Queue
# Stop Criterion: Find a node with no child.

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

# Solution 2: DFS with Recursion

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left or not root.right:
            if root.left:
                return 1 + self.minDepth(root.left)
            elif root.right:
                return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))