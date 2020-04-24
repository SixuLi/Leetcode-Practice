# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion
# When node.val > R, the whole right subtree of this node should be trimmed, so the trimmed binary
# tree must occur to the left of this onde.
# Similarly, when node.val < L, the trimmed binary tree must occur to the right of this node.
# Otherwise, we will trim both sides of the node.

# Time Complexity: O(N)
# Space Complexity: O(H) where H is the height of the tree

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def trim(root):
            if not root:
                return None
            elif root.val > R:
                return trim(root.left)
            elif root.val < L:
                return trim(root.right)
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
            return root