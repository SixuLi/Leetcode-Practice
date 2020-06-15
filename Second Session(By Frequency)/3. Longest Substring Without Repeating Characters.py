# Solution 1: Brute Force

# Time Complexity: O(n^2)
# Space Complexity: O(min(m,n)) where n is the length of string and m is the
# number of alphabets.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        n = len(s)

        for i in range(n):
            Set = set()
            Set.add(s[i])
            for j in range(i + 1, n):
                if s[j] in Set:
                    break
                else:
                    Set.add(s[j])
            res = max(len(Set), res)

        return res

# Solution 2: Sliding Window

# Time Complexity: O(n)
# Space Complexity: O(min(m,n))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        i, j = 0, 0
        Set = set()
        res = 0

        while i < n and j < n:
            if s[j] not in Set:
                Set.add(s[j])
                j += 1
                res = max(res, len(Set))
            else:
                Set.remove(s[i])
                i += 1

        return res
















