# Solution 1: Fast Power Algorithm Recursive
# Assume that we have got the result of x^(n/2), and now we want to
# get the result of x^n. Let A be result of x^(n/2), we can talk about
# x^n based on the parity of n respectively. If n is even, we can use
# the formula (x^n)^2 = x^(2*n) to get x^n = A*A. If n is odd, then
# A*A = x^(n-1). Intuitively, we need to multiply another x to the
# result, so x^n = A*A*x.

# Time Complexity: O(logn)
# Space Complexity: O(logn)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x*self.myPow(x, n-1)

# Solution 2: Fast Power Algorithm Iterative
# Change the recursive version in Solution 1 into Iteration

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n != 0:
            if n % 2 != 0:
                res *= x
            x *= x
            n //= 2
        return res
















