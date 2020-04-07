# Solution 1: Dynamic Programming
# Assume that G(n) represents the numbers of all the unique BSTs with n node.
# Denote F(i, n) as the numbers of BSTs with root i. (1<=i<=n)
# When we have root i, 1,...,i-1 should at left sub-tree and i+1,..,n should at right sub-tree.
# Then we have following iterative formulas:
# G(n) = F(1,n) + F(2,n) + ... + F(n,n); G(0)=1; G(1)=1;
# F(i,n) = G(i-1)*(n-i) (1<=i<=n)
# Finally, we can obtain that,
# G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-1)*G(0)

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            count = 0
            for j in range(1, i+1):
                count += dp[j-1]*dp[i-j]
            dp.append(count)
        return dp[-1]