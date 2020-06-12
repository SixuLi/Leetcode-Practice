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

# Solution 2: Binary Search
# For x >= 2, the square root is always smaller than x/2 and larger than 0.
# Therefore, the problem goes down to the iteration over the sorted set of integer.
# Then, we can use binary search.

# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid + 1


















