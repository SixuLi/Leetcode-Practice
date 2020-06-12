# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Solution 1: Hash Table
# We solve this problem in two loops:
# In the first loop, we scan the original linked list and make a copy of each node,
# and use hash table to connect the original node and copy node.
# In the second loop, we scan the original linked list and connect all the copy node.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        Dict = dict()
        while p:
            node = Node(p.val)
            Dict[p] = node
            p = p.next
        res = Dict[head]
        q = res
        while head:
            if head.next:
                Next = Dict[head.next]
                q.next = Next
            if head.random:
                q.random = Dict[head.random]
            q = q.next
            head = head.next
        return res

# Solution 2: Constant Space

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        while p:
            node = Node(p.val)
            node.next = p.next
            p.next = node
            p = p.next.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        p_old = head
        p_new = head.next
        res = p_new
        while p_old:
            p_old.next = p_old.next.next
            p_new.next = p_new.next.next if p_new.next else None
            p_old = p_old.next
            p_new = p_new.next
        return res
















