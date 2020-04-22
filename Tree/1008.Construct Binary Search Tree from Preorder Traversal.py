# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Construct a BST from preorder and inorder traversal
# Because inorder traversing a BST will give an ascending list, so, when we know all the element in a BST,
# we actually know the inorder traversal of it. Therefore, we can construct it from preorder and inorder traversal.

# Time Complexity: O(NlogN)
# Space Complexity: O(N)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        val = preorder[0]
        index = inorder.index(val)
        root = TreeNode(val)
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

# Solution 2: Recursion
# Since we are dealing with BST here, we can locate the current element in the original tree with the help of
# lower and upper limits.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)
        self.index = 0

        def helper(lower=float('-inf'), upper=float('inf')):
            if self.index == n:
                return None
            val = preorder[self.index]
            if val < lower or val > upper:
                return None
            self.index += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        return helper()

# Solution 3: Iteration
# Change the Solution 2 into iteration framework.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)
        if not n:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                node = stack.pop()
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            stack.append(child)
        return root



























