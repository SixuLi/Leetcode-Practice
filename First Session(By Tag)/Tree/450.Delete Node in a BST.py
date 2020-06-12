# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solultion 1: Recursion
# After we find the target node, there are three cases:
# 1. The node is a leaf.
# In this case, we just set node = None.

# 2. The node has a right child.
# In such a case, we first find the successor of this node and use the successor to replace it.
# And then, recursively delete the successor in the right subtrees.

# 3. The node has no right child, but left child.
# In this case, we first find the predecessor of the target node and use the predecessor to replace it.
# And then, recursively delete the predecessor in the left subtrees.

# Time Complexity: O(H)
# Space Complexity: O(H) to keep the recursion stack.

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # Delete from the right subtrees
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Delete from the left subtrees
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Delete current node
        else:
            # The node is a leaf
            if not root.left and not root.right:
                root = None

            # The node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

            # The node has no right child, but a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val






















