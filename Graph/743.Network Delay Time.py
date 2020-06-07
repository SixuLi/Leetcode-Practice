# Solution 1: Dijkstra Algorithm

# Time Complexity: O(ElogE), where E is the number of edges and V is the number of Vertexes
# Space Complexity: O(E + V)

from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        pq = [(0, K)]
        Dict = {}

        while pq:
            time, node = heapq.heappop(pq)
            if node not in Dict:
                Dict[node] = time
                for target, t_time in graph[node]:
                    if target not in Dict:
                        heapq.heappush(pq, (time + t_time, target))

        return max(Dict.values()) if len(Dict) == N else -1
