# Solution 1: Two Pointers + Hash Table

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        maxLen = 0
        used = set()
        while right < len(s):
            if s[right] not in used:
                used.add(s[right])
                right += 1
                maxLen = max(maxLen, len(used))
            else:
                used.remove(s[left])
                left += 1
        return maxLen