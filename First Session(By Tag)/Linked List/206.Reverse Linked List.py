# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Reverse linked list by copy into a list

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        res = ListNode(0)
        p = res
        for val in reversed(s):
            p.next = ListNode(val)
            p = p.next
        return res.next

# Solution 2: Modified the linked list in place(Iterative)

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nextTemp = cur.next
            cur.next = pre
            pre = cur
            cur = nextTemp
        return pre

# Solution 3: Recursive Version

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p










