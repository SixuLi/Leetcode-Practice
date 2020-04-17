# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Recursion
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, path = [], ""
        self.dfs(root, res, path)
        return res

    def dfs(self, root, res, path):
        if not root.left and not root.right:
            path = path + str(root.val)
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, res, path + str(root.val) + "->")
        if root.right:
            self.dfs(root.right, res, path + str(root.val) + "->")

# Solution 2: Iteration with Queue

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, path = [], ""
        queue = [(root, str(root.val))]
        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:
                res.append(path)
            else:
                if node.left:
                    queue.append((node.left, path+"->"+str(node.left.val)))
                if node.right:
                    queue.append((node.right, path+"->"+str(node.right.val)))
        return res

