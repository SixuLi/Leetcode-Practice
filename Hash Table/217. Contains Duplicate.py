# Solution 1: Hash Table

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Dict = dict()
        for num in nums:
            if num in Dict:
                return True
            else:
                Dict[num] = 1
        return False