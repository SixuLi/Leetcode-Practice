# Solution 1: Greedy

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = nums[0]
        res = nums[0]
        n = len(nums)

        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            res = max(res, curr_sum)

        return res