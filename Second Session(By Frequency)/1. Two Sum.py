# Solution 1: Hash Table

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for idx, num in enumerate(nums):
            if target - num not in Dict:
                Dict[num] = idx
            else:
                return [idx, Dict[target-num]]