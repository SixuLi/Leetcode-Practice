# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS
# Because the path does not need to start or end at the root or a leaf, we need to begin at each node
# to find the valid path.

# Time Complexity: O(N^2)
# Space Complexity: O(H), where H is the height of tree.

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        if not root:
            return 0
        stack = [root]
        while stack:
            node = stack.pop()
            self.dfs(node, sum)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return self.res

    def dfs(self, root, sum):
        if not root:
            return
        if root.val == sum:
            self.res += 1
        self.dfs(root.left, sum - root.val)
        self.dfs(root.right, sum - root.val)

# Solution 2: Alternative code for Soluton 1

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, sum):
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.dfs(root.left, sum - root.val) + self.dfs(root.right, sum - root.val)
        return res

