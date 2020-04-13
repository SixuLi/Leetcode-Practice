# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This question requires us to flip the tree upside down. Specifically, let the leftmost leaf
# to be the new root and for given node, let the right sibling to be it's left child and it parent
# to be it's right child.

# Solution 1: DFS with Recursion

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        return self.dfs(root, None)

    def dfs(self, p, parent):
        if not p:
            return parent
        root = self.dfs(p.left, p)
        if parent:
            p.left = parent.right
        else:
            p.left = None
        p.right = parent
        return root

# Solution 2: Iteration

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        # Start from root.
        cur, pre, preRight = root, None, None
        while cur:
            # Temporarily store 'cur.left' and 'cur.right' ('cur.left' will be next 'cur').
            temp1, temp2 = cur.left, cur.right
            # Modify parent-child links.
            cur.left, cur.right = preRight, pre
            # Go to next iteration.
            cur, pre, preRight = temp1, cur, temp2
        return pre

















