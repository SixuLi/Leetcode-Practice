# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Solution 1: DFS with Recursion
# For a given node, if it has right child, we need to let it left child point to the right child.
# Besides, if this node has next node, we need to point from the subtree of this node to the subtree of
# the next node, i.e., node.right.next -> node.next.left.

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

# Solution 2: BFS with Queue

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        return root
