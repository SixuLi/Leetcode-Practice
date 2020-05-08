# Solution 1: Hash Map
# We collect numbers and their counts from one of the arrays into
# a hash map. Then, we iterate along the second array, and check
# if the number exists in the hash map and its count is positive.
# If so, add the number to the result and decrease its count in
# the hash map.
# It's a good idea to check array sizes and use a hash map for the
# smaller array. It will reduce memory usage when one of the arrays
# is very large.

# Time Complexity: O(n+m)
# Space Complexity: O(min(n, m))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        Dict = dict()
        res = []
        for num in nums1:
            Dict[num] = Dict.get(num, 0) + 1
        for num in nums2:
            if num in Dict:
                if Dict[num] > 0:
                    res.append(num)
                    Dict[num] -= 1
        return res

# Solution 2: Sort
# Algorithm:
# 1. Sort nums1 and nums2
# 2. Initial i = j = 0
# 3. Move indices i along nums1 and j for nums2:
#    Increment i if nums1[i] is smaller.
#    Increment j if nums2[j] is smaller.
#    If nums1[i] == nums2[j], increment them both and add it to the result.

# Time Complexity: O(nlogn + mlogm)
# Space Complexity: O(1) for extra

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

# Follow up:
# What if elements of nums2 are stored on disk, and the memory is
# limited such that you cannot load all elements into the memory
# at once?

# Answer:
# If nums1 fits into the memory, we can use Solution 1 to collect
# counts for nums1 into a hash map. Then, we can sequentially load
# and process nums2.
# If neither of the arrays fir into the memory, we can apply some
# partial processing strategies:
# (1). Split the numeric range into subranges that fits into the
# memory. Modify Solution 1 to collect counts only within a given
# subrange, and call the method multiple times.
# (2). Use an external sort for both arrays. Modify Solution 2 to
# load and process arrays sequentially.

















