# Solution 1:
# This question is similar to question 33, but here, nums may contain duplicates.
# So, under this circumstance, nums[left] and nums[right] could be equal. If we directly use
# the same method in question 33, we may fail to distinguish which part is in order.
# Consider example: nums = [1, 3, 1, 1, 1] and target = 3.

# Note that nums[left] >= nums[right] and the above problem appears only when nums[left] == nums[right].
# Therefore, we can solve this problem by find the first element that not equals to nums[right] at left.
# And then begin original binary search.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False