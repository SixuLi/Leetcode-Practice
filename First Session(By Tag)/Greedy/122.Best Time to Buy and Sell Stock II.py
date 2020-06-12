# Solution 1: Peak and Valley Approach

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        valley = prices[0]
        peak = prices[0]
        i = 0
        max_profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]   # Find a Valley
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]     # Find a Peak
            max_profit += peak - valley

        return max_profit