# Solution 1: Max Heap
# Maintain a max heap with size k, after go through all the points, the points left in the max heap
# are the K closest points to origin.

# Time Complexity: O(nlogk)
# Space Complexity: O(k)
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            if i <= K-1:
                heapq.heappush(heap, (-distance, i))
            else:
                heapq.heappushpop(heap, (-distance, i))
        res = [points[idx[1]] for idx in heap]
        return res