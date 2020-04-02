# Solution 1: Merge Lists one by one
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time Complexity: O(K*N) Not good
# Space Complexity: O(N)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        dummy = ListNode(0)
        dummy.next = lists[0]
        for i in range(1, len(lists)):
            q = lists[i]
            while q:
                p1, p2 = dummy, dummy.next
                while p2 and p2.val < q.val:
                    p2 = p2.next
                    p1 = p1.next
                if p2:
                    new = ListNode(q.val)
                    new.next = p1.next
                    p1.next = new
                else:
                    p1.next = ListNode(q.val)
                q = q.next
        return dummy.next

# Solution 2: Merge with Divide and Conquer
# Time Complexity: O(N*LogK)
# Space Complexity: O(1)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next



















