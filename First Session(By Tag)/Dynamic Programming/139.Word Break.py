# Solution 1: Dynamic Programming
# Assume that dp is an array that contains booleans
# dp[i] is True if there if a word in the dictionary that ends at i-th index of s,
# and dp is also True at the beginning of the word.

# Time Complexity: O(N^2), where N is the length of s.
# Space Complexity: O(N)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for w in wordDict:
                if s[i-len(w):i] == w and dp[i-len(w)]:
                    dp[i] = True
        return dp[-1]

# Solution 2: BFS
# Modeled as a graph problem -- every index is a vertex and every edge is a completed word.
# The probelm thus boil down to if a path exists.

# Time Complexity: O(N^2)
# Space Complexity: O(N)

import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = collections.deque()
        visited = set()
        queue.appendleft(0)
        visited.add(0)
        while len(queue) > 0:
            cur_index = queue.pop()
            for i in range(cur_index, len(s)+1):
                if i in visited:
                    continue
                if s[cur_index:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    visited.add(i)
        return False