# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: InOrder Traversal(Recursion)
# The drawback of this approach is that we need to go through the whole inorder traversal, which actually is not
# necessary when we only need to find the kth smallest element in a BST.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = []
        self.inorder(root)
        return self.res[k - 1]

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

# Solution 2: InOrder Traversal(Iteration)
# When using Iterative approach, we can stop traverse when we have visited k elements.

# Time Complexity: O(H+k), where H is the height of the tree, i.e., H = logN.
# Space Complexity: O(H+k).

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


















