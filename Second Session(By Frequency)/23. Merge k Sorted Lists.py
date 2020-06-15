# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Heap

# Time Complexity: O(nlogk)
# Space Complexity: O(k)

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        dummy = ListNode(0)
        p = dummy
        heap = []

        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))

        while heap:
            val, idx = heapq.heappop(heap)

            p.next = ListNode(val)
            p = p.next

            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, (lists[idx].val, idx))

        return dummy.next


