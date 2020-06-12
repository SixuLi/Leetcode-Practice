# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # One of the node has been found. Return it.
        if root.val == p.val or root.val == q.val:
            return root

        # Look for both in both left subtree and right subtree.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in different subtrees. Then, the current root is the LCA.
        if left and right:
            return root

        # If neither p and q in this subtree, return none and backtrack.
        elif not left and not right:
            return None

        # If one of p and q is found in subtree, return that subtree.
        else:
            return left if left else right