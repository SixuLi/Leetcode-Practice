# Solution 1: Expand Around Center

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        if len(s) == 2 and s[0] == s[1]:
            return s

        res = ''
        n = len(s)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l + 1:r]

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l + 1:r]

        return res
