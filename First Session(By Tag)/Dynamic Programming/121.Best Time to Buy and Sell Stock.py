# Solution 1: One Pass Solution

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit, minprice = 0, float('inf')
        for price in prices:
            if price < minprice:
                minprice = price
            else:
                maxprofit = max(maxprofit, price - minprice)
        return maxprofit