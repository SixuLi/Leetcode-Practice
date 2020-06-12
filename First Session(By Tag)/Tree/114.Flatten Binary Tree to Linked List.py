# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: PreOrder
# First, we use preorder traversal to save each node in a list and then scan this list and let left child of each
# node is None and right child is the next node.
# Cons: We need to use additional O(N) Space.

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]

    def preOrder(self, root, res):
        if not root:
            return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)

# Solution 2: Recursion
# For a given root, we first flatten the left subtree and right subtree into to linked list, and next,
# we put the left subtree at the position of right child of root, and finally, put the original right subtree
# at the end of the linked list.

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = root.left
        right = root.right
        root.left = None
        self.flatten(left)
        self.flatten(right)
        root.right = left
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = right





















