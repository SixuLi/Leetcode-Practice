# Solution 1:
# Key idea: Sort the array first.

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = set()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums[i + 1:], -nums[i])

        return list(self.res)

    def twoSum(self, nums, target):
        Dict = dict()

        for i in range(len(nums)):
            if target - nums[i] not in Dict:
                Dict[nums[i]] = i
            else:
                self.res.add((-target, nums[i], target - nums[i]))