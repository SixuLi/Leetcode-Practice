# Solution 1: Sort Two List
# Given a string, the sorted version of it is unique.

# Time Complexity: O(mlogm + nlogn), where m = len(s) and n = len(t)
# Space Complexity: O(m+n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))

# Solution 2: Hash Table

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0]*26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for count in counter:
            if count < 0:
                return False
        return True