# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Solution 1: Convert linked list to array and DFS

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return self.dfs(nodes)
    def dfs(self, nodes):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = ListNode(nodes[mid])
        root.left = self.dfs(nodes[:mid])
        root.right = self.dfs(nodes[mid+1:])
        return root

# Solution 2: Inorder Simulation

# Time Complexity: O(n)
# Space Complexity: O(logn)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Get the size of the linked list first
        size = self.findsize(head)

        # Recursively form a BST out of linked list from l to r.
        def convert(l, r):
            nonlocal head
            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal.
            # Recursively form the left half.
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node.
            node = ListNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm.
            head = head.next

            # Recurse on the right hand side and form BST out of them.
            node.right = convert(mid + 1, r)
            return node

        return convert(0, size - 1)

    def findsize(self, head):
        p = head
        c = 0
        while head:
            c += 1
            head = head.next
        return c













