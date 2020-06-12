# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Recursion and Hash Table
# Similar to Solution 2 in Problem 105.

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        indexDict = {v: i for i, v in enumerate(inorder)}
        return self.buildTreeRec(postorder, indexDict, 0, len(inorder) - 1)

    def buildTreeRec(self, postorder, indexDict, beg, end):
        if beg > end:
            return None
        node = TreeNode(postorder.pop())
        index = indexDict[node.val]
        node.right = self.buildTreeRec(postorder, indexDict, index + 1, end)
        node.left = self.buildTreeRec(postorder, indexDict, beg, index - 1)
        return node

