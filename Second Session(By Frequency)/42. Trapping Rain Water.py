# Solution 1: Brute Force(TLE)

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0

        for i in range(1, len(height) - 1):
            left_max, right_max = 0, 0
            for l in range(i, -1, -1):
                left_max = max(left_max, height[l])
            for r in range(i, len(height)):
                right_max = max(right_max, height[r])
            res += min(left_max, right_max) - height[i]

        return res

# Solution 2: Dynamic Programming

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j])

        res = 0
        for i in range(1, n - 1):
            res += min(left_max[i], right_max[i]) - height[i]

        return res

# Solution 3: Two Pointers
# From the dynamic programming approach, notice that as long as
# right_max > left_max, the water trapped depends on the left_max,
# and else, depends on right_max. Therefore, we can use two pointers
# approach to solve this problem.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left_max, right_max = 0, 0
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    res += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    res += right_max - height[r]
                r -= 1

        return res



















