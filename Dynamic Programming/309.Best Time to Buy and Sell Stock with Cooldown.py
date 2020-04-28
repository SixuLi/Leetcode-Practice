# Solution 1: Dynamic Programming
# In this problem, we can have three states:
# 1. State A: hold stock, can sell.
# 2. Just sold stock, only can rest.
# 3. rest, can buy stock.

# Now, we analyze how to get each state one by one.
# State A: We can do nothing and stay at state A or change the state C to state A, i.e., buy the stock.
# State B: Transfer from state A to state B, i.e, sell the stock.
# State C: Do nothing and stay at state C or change the state B to state C, i.e., rest.

# Therefore, we can obtain the updating formula:
# StateA[i] = max(StateA[i-1], StateC[i-1] - prices[i])
# StateB[i] = StateA[i-1] + prices[i]
# StateC[i] = max(StateB[i-1], StateC[i-1])

# And we initilize the three states as:
# StateA[0] = -prices[0]
# StateB[0] = INT_MIN
# StateC[0] = 0

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        s1 = [0]*n
        s2 = [0]*n
        s3 = [0]*n
        s1[0] = -prices[0]
        s2[0] = float('-inf')
        s3[0] = 0
        for i in range(1, n):
            s1[i] = max(s1[i-1], s3[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
            s3[i] = max(s3[i-1], s2[i-1])
        return max(s2[-1], s3[-1])

# Solution 2: Dynamic Programming(O(1) space)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        A = -prices[0]
        B = float('-inf')
        C = 0
        for i in range(1, n):
            preB = B
            A = max(A, C-prices[i])
            B = A + prices[i]
            C = max(preB ,C)
        return max(B ,C)






















