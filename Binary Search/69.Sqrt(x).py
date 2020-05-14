# Solution 1: Brute Force

# Time Complexity: O(n^(1/2))
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1 or x == 2:
            return 1
        for i in range(x):
            if i*i > x:
                return i-1