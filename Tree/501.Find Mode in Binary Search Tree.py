# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Counter with Hash Table
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        Dict = self.inorder(root)
        maxmode = max(Dict.values())
        return [node for node, count in Dict.items() if count == maxmode]

    def inorder(self, root):
        Dict = {}
        stack = []
        in_order = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val in Dict:
                Dict[root.val] += 1
            else:
                Dict[root.val] = 1
            root = root.right
        return Dict