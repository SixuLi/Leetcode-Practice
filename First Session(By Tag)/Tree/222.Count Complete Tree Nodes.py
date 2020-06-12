# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion(Trivial method and does not utilize the property of Complete Binary Tree)

# Time Complexity: O(N)
# Space Complexity: O(logN)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1+self.countNodes(root.left)+self.countNodes(root.right) if root else 0

# Solution 2: Binary Search
# We know that in a complete binary tree, every level except possibly the last, is completely filled and all
# nodes in the last level are as left as possible. Assume that the depth of complete binary tree is d, it has
# 2^d-1 nodes on all levels except the last one. So, what we need to do is to figure out how many nodes exist
# in the last level.
# There potential 2^d nodes exist in the last level, so, in the inner loop, we can check whether the index-th node
# exists in it by using binary seach. And in the out loop, we use binary search to find the rightest index may exist.

# Time complexity: O(log^2(N))
# Space Complexity: O(1)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = self.depth(root)
        if d == 0:
            return 1
        left, right = 1, 2 ** d - 1
        while left <= right:
            pivot = (left + right) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return 2 ** d - 1 + left

    def depth(self, root):
        if not root:
            return 0
        d = 0
        while root.left:
            root = root.left
            d += 1
        return d

    def exists(self, index, d, root):
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = (left + right) // 2
            if index <= pivot:
                root = root.left
                right = pivot
            else:
                root = root.right
                left = pivot + 1
        return root is not None

























