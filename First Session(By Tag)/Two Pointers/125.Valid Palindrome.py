# Solution 1: Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l, r = 0, len(s)-1
        while l <= r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
            elif s[l].isalnum() == False:
                l += 1
            else:
                r -= 1
        return True