# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Iteration
# Key Property: Inorder traverse a BST will give us a ascending order of the tree.
# Obviously, in this problem, we need to inorder traverse the BST. During the traversal, we use variable pre to record
# the value of the last ancestor of current node. If pre == p.val, the current node is what we want to find.

# Time Complexity: O(1) in best case and O(N) in the worst case.
# Space Complexity: O(H) where H is the tree Height

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        stack = []
        pre = float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre == p.val:
                return root
            pre = root.val
            root = root.right
        return None

