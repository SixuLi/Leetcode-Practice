# Solution 1: DFS
# Key idea: Build a graph based on the given list of undirected edges.

# Time Complexity: O(V+E)
# Space Complexity: O(V+E)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        visited = set()
        res = 0

        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)

        def dfs(i):
            if i not in visited:
                visited.add(i)
                for j in graph[i]:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res