# Solution 1: BFS

# Time Complexity: O(m*n)
# Space Complexity: O(m*n) in the worst case.

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if rooms:
            queue = deque()
            m,n = len(rooms), len(rooms[0])
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for i in range(m):
                for j in range(n):
                    if rooms[i][j] == 0:
                        queue.append((i, j, 0))

            while queue:
                r, c, distance = queue.popleft()
                for d in directions:
                    nr, nc = r+d[0], c+d[1]
                    if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] >= 2**30 :
                        rooms[nr][nc] = distance + 1
                        queue.append((nr, nc, distance+1))



