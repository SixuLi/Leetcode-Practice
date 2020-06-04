# Solution 1: DFS

# Time Complexity: O(m*n), where m = len(matrix), n = len(matrix[0])
# Space Complexity: O(m*n)

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            self.dfs(matrix, p_visited, i, 0, m, n)
            self.dfs(matrix, a_visited, i, n - 1, m, n)

        for j in range(n):
            self.dfs(matrix, p_visited, 0, j, m, n)
            self.dfs(matrix, a_visited, m - 1, j, m, n)

        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, visited, i, j, m, n):
        visited[i][j] = True
        for d in self.directions:
            ni, nj = i + d[0], j + d[1]
            if ni < 0 or ni >= m or nj < 0 or nj >= n or visited[ni][nj] or matrix[i][j] > matrix[ni][nj]:
                continue
            self.dfs(matrix, visited, ni, nj, m, n)

# Solution 2: BFS + Set

# Time Complexity: O(m*n)
# Space Complexity: O(m*n) in the worst case.

from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])

        pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
        atlantic = set([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)])
        return list(self.bfs(matrix, pacific) & self.bfs(matrix, atlantic))

    def bfs(self, matrix, reachable_ocean):
        queue = deque(reachable_ocean)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if self.isValid(matrix, nr, nc) and (nr, nc) not in reachable_ocean and matrix[nr][nc] >= matrix[r][c]:
                    queue.append((nr, nc))
                    reachable_ocean.add((nr, nc))
        return reachable_ocean

    def isValid(self, matrix, i, j):
        m, n = len(matrix), len(matrix[0])
        if 0 <= i < m and 0 <= j < n:
            return True
        return False

