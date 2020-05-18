# Solution 1: Floyd's Tortoise and Hare

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        t, r = head, head.next
        while t.next and r.next and r.next.next:
            if t == r:
                return True
            else:
                t = t.next
                r = r.next.next
        return False

# Solution 2: Hash Table

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        Set = set()
        while head:
            if head in Set:
                return True
            else:
                Set.add(head)
            head = head.next
        return False

















