# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Iteration

# Time Complexity: O(m+n)
# Space Complexity: O(m+n)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:
            if l1.val > l2.val:
                p.next = ListNode(l2.val)
                l2 = l2.next
            else:
                p.next = ListNode(l1.val)
                l1 = l1.next
            p = p.next

        p.next = l1 if l1 else l2

        return dummy.next

