# Solution 1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        p = head
        while l1 and l2:
            cur = l1.val + l2.val + carry
            if cur >= 10:
                carry = 1
            else:
                carry = 0
            val = cur % 10
            p.next = ListNode(val)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur = l1.val + carry
            if cur >= 10:
                carry = 1
            else:
                carry = 0
            val = cur % 10
            p.next = ListNode(val)
            p = p.next
            l1 = l1.next
        while l2:
            cur = l2.val + carry
            if cur >= 10:
                carry = 1
            else:
                carry = 0
            val = cur % 10
            p.next = ListNode(val)
            p = p.next
            l2 = l2.next
        if carry != 0:
            p.next = ListNode(carry)
            p = p.next
        return head.next