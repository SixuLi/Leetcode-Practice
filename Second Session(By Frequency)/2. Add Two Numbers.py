# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1:

# Time Complexity: O(max(len(l1), len(l2)))
# Space Complexity: O(max(len(l1), len(l2)))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        carry = 0

        while l1 and l2:
            cur = l1.val + l2.val + carry
            if cur >= 10:
                carry = 1
                cur = cur % 10
            else:
                carry = 0
            p.next = ListNode(cur)
            p = p.next
            l1 = l1.next
            l2 = l2.next

        l = l1 if l1 else l2

        while l:
            cur = l.val + carry
            if cur >= 10:
                carry = 1
                cur = cur % 10
            else:
                carry = 0
            p.next = ListNode(cur)
            p = p.next
            l = l.next

        if carry == 1:
            p.next = ListNode(carry)
            p = p.next
            carry = 0

        return dummy.next

