# Solution 1: Copy the linked list into a list and use Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


# Solution 2: Reverse the Second Half of Linked List in-place

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # Find the end of the first half.
        first_half_end = self.end_of_first_half(head)
        # Find the begin of the second half.
        second_half_start = self.reverse_list(first_half_end.next)

        first_position = head
        second_position = second_half_start

        # Test whether is palindrome.
        while first_position and second_position:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next
        return True

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        pre = None
        cur = head
        while cur:
            nextTemp = cur.next
            cur.next = pre
            pre = cur
            cur = nextTemp
        return pre

















