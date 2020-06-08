# Solution 1: Dijkstra's Algorithm

# Time Complexity: O(V + ElogV)
# Space Complexity: O(E+V)

from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if not flights or not flights[0]:
            return -1

        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))

        res = 0
        pq = [(0, src, K + 1)]

        while pq:
            cost, cur, k = heapq.heappop(pq)
            if cur == dst:
                return cost

            if k > 0:
                for end, price in graph[cur]:
                    heapq.heappush(pq, (cost + price, end, k - 1))
        return -1