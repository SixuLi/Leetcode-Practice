# Solution 1: Brute Force(TLE)

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        minLen = float('inf')
        for i in range(len(nums)):
            cur = nums[i]
            if cur >= s:
                return 1
            for j in range(i+1, len(nums)):
                cur += nums[j]
                if cur >= s:
                    minLen = min(minLen, len(nums[i:j+1]))
                    break
        return minLen

# Solution 2: Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = left = 0
        minLen = float('inf')
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                minLen = min(minLen, right - left + 1)
                total -= nums[left]
                left += 1
        return minLen if minLen <= len(nums) else 0















