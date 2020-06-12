# Solution 1: Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        count = 0
        for idx, num in enumerate(nums):
            if num != 0:
                nums[p] = num
                p += 1
            else:
                count += 1
        for i in range(len(nums)-1, len(nums) - count - 1, -1):
            nums[i] = 0