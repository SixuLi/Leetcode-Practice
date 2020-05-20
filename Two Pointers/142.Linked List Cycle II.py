# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1: Floyd's Tortoise and Hare

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hare = self.getIntersect(head)
        if not hare:
            return None
        else:
            tortoise = head
            while tortoise != hare:
                tortoise = tortoise.next
                hare = hare.next
            return tortoise

    def getIntersect(self, head):
        tortoise = head
        hare = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return hare
        return None

# Solution 2: Hash Table

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        Set = set()
        while head:
            if head in Set:
                return head
            else:
                Set.add(head)
                head = head.next
        return None

















