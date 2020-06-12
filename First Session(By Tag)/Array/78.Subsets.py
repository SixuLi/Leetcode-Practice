# Solution 1: Dynamic Programming
# Assume tha all the subset for the front i element is dp[i], then,
# dp[i] consists two parts:
# 1. dp[i-1]
# 2. The combinations of the ith element with every elements in dp[i-1]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [[num] + pre for pre in res]
        return res

# Solution 2: Backtracking
# Loop over the length of combinations, and generate all the combinations given length with the help of backtracking.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, cur = []):
            # If the combination is done
            if len(cur) == k:
                output.append(cur[:])
            for i in range(first, n):
                # Add nums[i] into the current combination
                cur.append(nums[i])
                # Use the next integers to complete the combination
                backtrack(i+1, cur)
                # Backtrack
                cur.pop()
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return output