# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

# Solution 2: Improve the Recursion
# In Solution 1, every time we try to find the index of the root of subtree in array inorder, we may need to
# go through the whole array, which makes the algorithm become slow.
# Therefore, we can use Hash Table to solve this problem.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder.reverse()
        indexDict = {v: i for i, v in enumerate(inorder)}
        return self.buildTreeRec(preorder, indexDict, 0, len(preorder) - 1)

    def buildTreeRec(self, preorder, indexDict, beg, end):
        if beg > end:
            return None
        node = TreeNode(preorder.pop())
        index = indexDict[node.val]
        node.left = self.buildTreeRec(preorder, indexDict, beg, index - 1)
        node.right = self.buildTreeRec(preorder, indexDict, index + 1, end)
        return node