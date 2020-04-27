# Solution 1: Brute-Force Enumeration(Time Limit Exceeded)
# Based on the problem, we can have the formula:
# numSquares(n) = min(numSquares(n-k) + 1) for all k in {square numbers}

import math
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        def minNumSquares(k):

            # Bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k - square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)

# Solution 2: Dynamic Programming
# The problem of Solution 1 is that we recalculate the sub-solutions over and over again.
# So, we can use Dynamic Programming to solve this problem.

# Time Complexity: O(N^(3/2))
# Space Complexity: O(N)

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]

# Greedy Enumeration
# Starting from the combination of one single number to multiple numbers, once we find a combination
# that can sum up to the given number n, then we can say that we must have found the smallest
# combination, since we enumerate the combinations greedily from small to large.

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = set([i ** 2 for i in range(1, int(n ** 0.5) + 1)])

        def is_divided_by(n, count):
            if count == 1:
                return n in square_nums
            for square in square_nums:
                if is_divided_by(n - square, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count



















