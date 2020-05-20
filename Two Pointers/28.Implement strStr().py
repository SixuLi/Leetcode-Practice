# Solution 1: Two Pointers:

# Time Complexity: O((N-L)L)
# Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0

        pn = 0
        while pn < n - L + 1:
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            cur_len = pl = 0
            while pn < n and pl < L and haystack[pn] == needle[pl]:
                pl += 1
                pn += 1
                cur_len += 1

            if cur_len == L:
                return pn - L
            else:
                pn = pn - cur_len + 1
        return -1