# Solution 1: Minimum Heap

# Time Complexity: O(x + klogx), where x = min(n, k)
# Space Complexity: O(x)
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Preparing our min-Heap
        minHeap = []
        for r in range(min(n, k)):
            # Add triplets of information for each cell
            minHeap.append((matrix[r][0], r, 0))

        # Heapify our list
        heapq.heapify(minHeap)

        # Until we find k elements
        while k > 0:

            # Extract Min
            element, r, c = heapq.heappop(minHeap)

            # If we have any new elements in the current row, add them.
            if c < n - 1:
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))

            # Decrement k
            k -= 1

        return element