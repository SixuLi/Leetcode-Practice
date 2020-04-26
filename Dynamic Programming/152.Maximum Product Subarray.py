# Solution 1: Dynamic Programming
# Insights:

# What if the array has just positive numbers including zero?
# A solution of this will maintain max_prod[i] where max_prod[i] is the maximum
# subarray product ending at i-th position. Then the updating formula can be writen as
# max_prod[i+1] = max(max_prod[i] * nums[i+1], nums[i+1]).

# Now how do we change the solution when we allow negative numbers?
# Imagine that we have both max_prod[i] and min_prod[i], i.e, max prod and min prod ending at i-th position.
# Now if we have a negative number at nums[i+1] and if min_prod[i] is negative,
# then the product of the two will be positive and can potentially be largest product..

# So, we have three choices to make at any position in the array.
# 1. We can get maximum product by multiplying the current element with maximum product calculated so far.
# 2. We can get maximum product by multiplying the current element with minimum product calculated so far.
# 3. Current element might be a starting position for maximum product subarray.

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod, min_prod = x, y
            res = max(res, max_prod)
        return res