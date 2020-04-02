# Solution 1: One Pass Scan
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy
        while n > 0:
            q = q.next
            n -= 1
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next