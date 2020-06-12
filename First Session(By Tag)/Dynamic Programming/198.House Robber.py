# Solution 1: Dynamic Programming
# Let us denote,
# f(i) = Largest amount that we can rob from the first i houses.
# A(i) = Amount of money of the ith house.

# Let us look at the case n=1, clearly f(1) = A(1).
# And now for n=2, f(2) = max(A(1), A(2))
# For n=3, we have two options:
# 1. Rob the third house, and add its amount to the first house's amount.
# 2. Do not rob the third house, and stick with the maximum amount of the first two houses.
# Therefore, we can obtain the update formula as follows:
# f(i) = max(f(i-2)+A(i), f(i-1))

# Time Complexity: O(N)
# Space Complexity: O(N)(can be optimized to O(1))

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]