# Solution 1: Brute Force(TLE)
# Remove each edge once a time, and use DFS to test whether the left graph is still
# connected.

# Time Complexity: O((E+V)E), where E is the number of edge in the graph
# Space Complexity: O(E+V), where V is the number of vertex in the graph

from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if not connections:
            return []
        res = []

        for i in range(len(connections)):
            visited = [False] * n
            curr_connections = connections[:i] + connections[i + 1:]
            graph = self.makeGraph(curr_connections)
            visited[0] = True
            self.num = 1
            self.dfs(graph, visited, 0)
            if self.num != n:
                res.append(connections[i])

        return res

    def makeGraph(self, connections):
        graph = defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        return graph

    def dfs(self, graph, visited, node):
        for v in graph[node]:
            if not visited[v]:
                self.num += 1
                visited[v] = True
                self.dfs(graph, visited, v)

# Solution 2: Tarjan's Algorithm
# If detect a circle, discard it and the left edges are the critical edges we want to find.

# Time Complexity: O(V+E)
# Space Complexity: O(V+E)

import collections


class Solution(object):
    def criticalConnections(self, n, connections):
        def makeGraph(connections):
            graph = collections.defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = makeGraph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            rank[node] = n  # this line is not necessary. see the "brain teaser" section below
            return min_back_depth

        dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
        return list(connections)
