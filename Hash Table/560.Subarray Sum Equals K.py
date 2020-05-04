# Solution 1: Brute-Force(TLE)

# Time Complexity: O(N^2)
# Space Complexity: O(1)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                if cur == k:
                    count += 1
        return count

# Solution 2: Hash Table

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Dict = {0:1}
        count = 0
        sums = 0
        for num in nums:
            sums += num
            count += Dict.get(sums-k, 0)
            Dict[sums] = Dict.get(sums, 0) + 1
        return count