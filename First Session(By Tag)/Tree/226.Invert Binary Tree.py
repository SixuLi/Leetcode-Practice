# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Recursion
# In order to invert a binary tree, we can exchange the position of the left child and right child
# for a given node from top to bottom. And this can be writen in an recursion way.

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root.left and not root.right:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)

# Solution 2: Iteration

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root