# Solution 1: Hash Table

# Time Complexity: O(m+n)
# Space Complexity: O(min(m,n))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        res = set()
        for num in nums2:
            if num in set1:
                res.add(num)
        return [i for i in res]