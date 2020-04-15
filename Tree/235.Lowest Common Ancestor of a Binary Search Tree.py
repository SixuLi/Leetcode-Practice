# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1:
# We can search the given node in the BST and store all the ancestors of it. Then, in order to find LCA of two node,
# we can compare the two lists which store the ancestors and find the smallest one in common.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc1, anc2 = self.findAncestor(root, p.val), self.findAncestor(root, q.val)
        for i in range(min(len(anc1), len(anc2))):
            if anc1[i].val != anc2[i].val:
                break
        return anc1[i] if anc1[i] == anc2[i] else anc1[i - 1]

    def findAncestor(self, root, val):
        anc = []
        while True:
            anc.append(root)
            if root.val == val:
                return anc
            elif root.val > val:
                root = root.left
            else:
                root = root.right

# Solution 2: Recursion
# For the given two nodes p and q, when we do the search in BST, for the current node in tree,
# If p.val > node.val and q.val > node.val, then p and q are in the right subtree of this node,
# so we continue the search on the right subtree.
# If p.val < node.val and q.val < node.val, then p and q are in the left subtree of this node,
# so we continue the search on the left subtree.
# If not the two cases above, then this node is the one we want to find.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# Solution 3: Iteration
# Change the recursive approach in Solution 2 to iterative approach.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        while True:
            if p_val > root.val and q_val > root.val:
                root = root.right
            elif p_val < root.val and q_val < root.val:
                root = root.left
            else:
                return root


























