# Solution 1: Binary Search

# Time Complexity: O(log(min(m,n)))
# Space Complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = len(nums1), len(nums2)
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        lo, hi = 0, x
        while lo <= hi:
            partitionX = (lo + hi) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                hi = partitionX - 1

            else:
                lo = partitionX + 1