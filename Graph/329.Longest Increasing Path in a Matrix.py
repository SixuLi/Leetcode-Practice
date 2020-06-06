# Solution 1: Topological Sort

# Time Complexity: O(mn)
# Space Complexity: O(mn)

from collections import defaultdict, Counter, deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        graph = defaultdict(list)
        c = Counter()
        queue = deque()
        max_length = 0

        for i in range(m):
            for j in range(n):
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n and matrix[i][j] < matrix[ni][nj]:
                        graph[(i, j)].append((ni, nj))
                        c[(ni, nj)] += 1

        for i in range(m):
            for j in range(n):
                if (i, j) not in c:
                    queue.append((i, j))

        while queue:
            max_length += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for ni, nj in graph[(i, j)]:
                    c[(ni, nj)] -= 1
                    if c[(ni, nj)] == 0:
                        queue.append((ni, nj))

        return max_length
