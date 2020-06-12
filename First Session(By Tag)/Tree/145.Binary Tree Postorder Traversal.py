# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: DFS with Recursion

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.res.append(root.val)

# Solution 2: DFS with Iteration(Using Stack)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [], []
        # Push the left boundary first from the root.
        self.pushLeftNode(root, stack)
        while stack:
            top = stack[-1]
            if top[1]:
                # If the top node's right subtree is already visited.
                # Then we are done with this node.
                res.append(stack.pop()[0].val)
            else:
                # If the top node's right subtree has not been visited.
                # We visit the right subtree after change the signal of this node to be Ture.
                stack.append((stack.pop()[0], True))
                self.pushLeftNode(top[0].right, stack)
        return res

    def pushLeftNode(self, root, stack):
        while root:
            # False represents that the right subtree of this node has not been visited yet.
            stack.append((root, False))
            root = root.left