# Solution 1: Hash Table

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Dict = dict()
        for i in range(len(nums)):
            if nums[i] in Dict:
                if i - Dict[nums[i]][-1] <= k:
                    return True
                Dict[nums[i]].append(i)
            else:
                Dict[nums[i]] = [i]
        return False