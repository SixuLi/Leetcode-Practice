# Solution 1: Max Heap

# Time Complexity: O(n + klogn)
# Space Complexity: O(1)
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        return -res