# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Key Problem: For a given root, not only the right child should be large than it, but also
# all the elements in the right subtree. Similarly for the left subtree.

# Solution 1: Recursion
# One compares the root value with its upper and lower limits if they are available.
# Then one repeats the same step recursively for left and right subtrees.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root)

    def dfs(self, root, low=float('-inf'), upper=float('inf')):
        if not root:
            return True
        val = root.val
        if val <= low or val >= upper:
            return False
        if not self.dfs(root.right, val, upper):
            return False
        if not self.dfs(root.left, low, val):
            return False
        return True

# Solution 2: Iteration
# The above recursion method can be converted to iteration by using Stack.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, low, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= low or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, low, val))
        return True

# Solution 3: Inorder Traversal
# Let's consider the inorder traversal left -> node -> right. If we traverse BST with inorder,
# then, each element should be larger than previous one. Hence, we can use Stack to help use traverse
# with inorder.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, pre = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            val = root.val
            if val <= pre:
                return False
            pre = val
            root = root.right
        return True


















