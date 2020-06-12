# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution 1: Sort an Almost Sorted Array Where Two Elements are Swapped
# When inorder traverse a BST, we will obtain a ascending list. And in this problem, there are two
# nodes swapped. Therefore, we can first use inorder traversal to obtain the almost sorted list,
# and find the two problem nodes. Finally, we just swap the value of this two nodes and get the final result.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        in_order = self.inorder(root)
        x, y = self.two_swapped(in_order)
        x.val, y.val = y.val, x.val

    def inorder(self, root):
        if not root:
            return []
        in_order = []
        node = root
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                return in_order
            node = stack.pop()
            in_order.append(node)
            node = node.right

    def two_swapped(self, List):
        x, y = None, None
        for i in range(len(List) - 1):
            if List[i].val > List[i + 1].val:
                y = List[i + 1]
                if not x:
                    x = List[i]
                else:
                    break
        return x, y

# Solution 2: Find the Two Swapped Node during the Inorder Traversal

# Time Complexity: O(1) in the best case and O(N) in the worst case.
# Space Complexity: O(H)(at most store H node in the stack, where H is the tree height)

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if not x:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val

























