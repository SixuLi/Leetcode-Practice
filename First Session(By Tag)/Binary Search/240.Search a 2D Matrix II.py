# Solution 1: Binary Search

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if n == 0:
            return False
        for i in range(m):
            if matrix[i][0] > target:
                break
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

# Solution 2: Search Space Reduction
# First, we initialize a (row, col) pointer to the bottom-left of the matrix.
# Then, until we find the target, we do as following:
# If the current value is larger than target, we can move one row "up",
# otherwise, if the current value is smaller than target, we move one col "right".

# Time Complexity: O(m+n)
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if n == 0:
            return False
        row, col = m-1, 0
        while col < n and row >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False




















