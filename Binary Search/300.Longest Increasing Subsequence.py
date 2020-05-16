# Solution 1: Dynamic Programming
# Let dp[i] represent the LIS at position i, therefore,
# if nums[i] > nums[j], for 0 <= j < i, then,
# dp[i] = max(dp[i], dp[j] + 1)

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)