# Solution 1: Brute Force(TLE)
# For each element in the array, we find the maximum level of water
# it can trap after the rain, which is equal to the minimum of maximum
# height of bars on both the sides minus its own height.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        for i in range(len(height)):
            left_max, right_max = 0, 0
            for left in height[:i]:
                left_max = max(left, left_max)
            for right in height[i+1:]:
                right_max = max(right, right_max)
            res += max(min(left_max, right_max) - height[i], 0)
        return res

# Solution 2: Dynamic Programming
# In brute force, we iterate over the left and right parts again
# and again just to find the highest bar size upto that index.
# But this could be stored, i.e., Dynamic Programming.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        Len = len(height)
        left_max, right_max = [0] * Len, [0] * Len

        left_max[0] = height[0]
        for i in range(1, Len):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[-1] = height[-1]
        for i in range(Len - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        res = 0
        for i in range(Len):
            res += max(min(left_max[i], right_max[i]), 0) - height[i]
        return res

# Solution 3: Using Stack

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                res += distance * bounded_height
            stack.append(i)
        return res














