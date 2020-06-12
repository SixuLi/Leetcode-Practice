# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Preorder Traversal (Top Down Depth-first Search)
# Check condition:
# For a given node, if it's parent is None(means that this node is root)
# or node.val != parent.val+1(not consecutive sequence along this path), set length of path equal to 1.
# Elif length = length+1

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxlength = 0
        self.dfs(root, None, 0)
        return self.maxlength

    def dfs(self, node, parent, length):
        if not node:
            return
        length = length + 1 if parent and node.val == parent.val + 1 else 1
        self.maxlength = max(length, self.maxlength)
        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)

# Solution 2: DFS with Postorder Traversal(Bottom Up Depth-first Search)

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxlength = 0
        self.dfs(root)
        return self.maxlength

    def dfs(self, node):
        if not node:
            return 0
        l = self.dfs(node.left) + 1
        r = self.dfs(node.right) + 1
        if node.left and node.left.val != node.val + 1:
            l = 1
        if node.right and node.right.val != node.val + 1:
            r = 1
        self.maxlength = max(self.maxlength, max(l, r))
        return max(l, r)





















