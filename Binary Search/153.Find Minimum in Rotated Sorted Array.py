# Solution 1: Binary Search

# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # Two Pointers
        left, right = 0, n - 1

        # The original array is ascending
        if nums[left] < nums[right]:
            return nums[left]

        # Binary Search
        while left <= right:
            mid = (left + right) // 2

            # If the mid element is greater than its next element,
            # then mid+1 element is the smallest.
            # This point point would be the point of change. From higher to lower.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # If the mid element is lesser than its previous element,
            # then mid element is the smallest.
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # If the mid elements value is greater than the left element,
            # this means the least value is still somewhere to the right.
            if nums[mid] > nums[left]:
                left = mid + 1

            # If nums[left] is greater than the mid,
            # this means the smallest value is somewhere to the left.
            else:
                right = mid - 1