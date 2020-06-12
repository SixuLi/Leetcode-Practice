# Solution 1: BFS

# Time Complexity: O(m*n), where m is the number of row and n is the number
# of columns.
# Space Complexity: O(min(m, n))

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    res += 1
                    self.bfs(grid, r, c)
        return res

    def isValid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or r >= m or c < 0 or c >= n:
            return False
        return True

    def bfs(self, grid, r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'
        while queue:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if self.isValid(grid, nr, nc) and grid[nr][nc] == "1":
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
