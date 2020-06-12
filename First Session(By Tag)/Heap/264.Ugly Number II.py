# Solution 1:
# Iteratively generate all the ugly numbers.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i1, i2, i3 = 0, 0, 0
        while n > 1:
            u1, u2, u3 = 2*ugly[i1], 3*ugly[i2], 5*ugly[i3]
            umin = min(u1, u2, u3)
            if umin == u1:
                i1 += 1
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]