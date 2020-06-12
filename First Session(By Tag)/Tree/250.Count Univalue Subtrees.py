# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Given a node in the tree, there are two conditions that it can be an univalue subtree:
# 1. It is a leaf node, i.e., no child.
# 2. The two subtrees of this node are univalue subtrees and the node and it's children
# have the same value.

# Solution 1: DFS with Recursion
# Time Complexity: O(N)
# Space Complexity: O(logN)

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        self.is_unisub(root)
        return self.count

    def is_unisub(self, root):
        # Find an univalue subtree and increase the count
        if not root.left and not root.right:
            self.count += 1
            return True
        is_uni = True

        # Check if all of the node's children are univalue subtrees and if they have the same value
        if root.left:
            is_uni = self.is_unisub(root.left) and is_uni and root.val == root.left.val
        if root.right:
            is_uni = self.is_unisub(root.right) and is_uni and root.val == root.right.val
        # Increase the count and return whether an univalue tree exists here
        self.count += is_uni
        return is_uni

