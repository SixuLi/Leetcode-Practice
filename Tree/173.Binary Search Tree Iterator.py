# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1:
# Key property: The inorder traversal of a BST will give us the elements in a sorted order.

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self._inorder(root)
        self.index = -1

    # Using inorder traversal of BST to find the sorted nodes.
    def _inorder(self, root):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return
            root = stack.pop()
            self.nodes_sorted.append(root.val)
            root = root.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()