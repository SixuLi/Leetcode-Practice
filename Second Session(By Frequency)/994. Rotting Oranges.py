# Solution 1: BFS

# Time Complexity: O(mn)
# Space Complexity: O(mn) in the worst case

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        level = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c, level))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while queue:
            r, c, level = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, level + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return level
