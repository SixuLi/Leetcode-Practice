# Solution 1: Hash Table

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Dict = dict()
        for idx, num in enumerate(numbers):
            Dict[num] = idx
        for i in range(len(numbers)):
            if target - numbers[i] in Dict:
                idx1 = min(i, Dict[target - numbers[i]]) + 1
                idx2 = max(i, Dict[target - numbers[i]]) + 1
                return [idx1, idx2]

# Solution 2: Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1