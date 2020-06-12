# Solution 1: DFS

# Time Complexity: O(mn)
# Space Complexity: O(mn)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[True for _ in range(n)] for _ in range(m)]

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and visited[r][c]:
                    res += 1
                    self.dfs(grid, r, c, visited)
        return res

    def dfs(self, grid, r, c, visited):
        m, n = len(grid), len(grid[0])
        if 0 <= r < m and 0 <= c < n and visited[r][c] and grid[r][c] == '1':
            visited[r][c] = False
            self.dfs(grid, r - 1, c, visited)
            self.dfs(grid, r + 1, c, visited)
            self.dfs(grid, r, c - 1, visited)
            self.dfs(grid, r, c + 1, visited)

# Solution 2: BFS

# Time Complexity: O(mn)
# Space Complexity: O(min(m, n))

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[True for _ in range(n)] for _ in range(m)]

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    res += 1
                    self.bfs(grid, r, c)
        return res

    def bfs(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(r, c)])
        grid[r][c] = '0'

        while queue:
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'



















