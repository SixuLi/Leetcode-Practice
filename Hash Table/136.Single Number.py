# Solution 1: Hash Table

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Dict = dict()
        for num in nums:
            if num in Dict:
                Dict[num] += 1
            else:
                Dict[num] = 1
        for num in nums:
            if Dict[num] == 1:
                return num

# Solution 2: Math

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)

# Solution 3: Bit Operation
# Assume operator ^ represents XOR operation, then we have,
# a ^ 0 = a and a ^ a = 0.
# Therefore, we can use this operation to solve this problem.

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a














