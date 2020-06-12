# Solution 1: Binary Search

# Time Complexity: O(logn)
# Space Complexity: O(1)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid) == True:
                if isBadVersion(mid) == False:
                    return mid
                else:
                    hi = mid
            else:
                lo = mid + 1
        return lo

