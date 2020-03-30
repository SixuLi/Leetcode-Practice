# Solution 1:
# Using pointer i to point the fist position of current element and pointer j for the first position of
# the element that different from nums[i].
# If j-i >= 2, nums[i] need to be recorded again.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        i, j = 0, 1
        k = 0
        while i < n:
            while j < n and nums[i] == nums[j]:
                j += 1
            nums[k] = nums[i]
            k += 1
            if j - i >= 2:
                nums[k] = nums[i]
                k += 1
            i, j = j, j+1
        return k

# Solution 2:
# Using k to record the length of new array and while scanning, pointer k points to the position the new element
# will be place.
# We use pointer i to scan the whole array and if nums[i] != nums[k-2], we should store nums[i] at position k because
# the current new array does not contain more than two elements that equals to nums[i].


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        k = 2
        for i in range(2, n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k