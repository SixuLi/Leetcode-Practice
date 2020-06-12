# Solution 1: DFS
# Use a set to store the visited nodes.

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.visited = set()
        res = 0
        for i in range(len(M)):
            if i not in self.visited:
                res += 1
                self.dfs(M, i)
        return res

    def dfs(self, M, i):
        for j in range(len(M[i])):
            if M[i][j] == 1 and j not in self.visited:
                self.visited.add(j)
                self.dfs(M, j)
