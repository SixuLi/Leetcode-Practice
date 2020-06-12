# Solution 1: Binary Search
# When during the binary search, if the current position is at descending slope,
# the peak element will be found on left of this position and if it is at
# ascending slope, then the peak will on the right.

# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left   
