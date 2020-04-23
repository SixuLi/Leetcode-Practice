# Solution 1: Monotonic Decreasing Stack

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        stack = [float('inf')]
        res = 0
        for i in range(len(arr)):
            while stack[-1] <= arr[i]:
                drop = stack.pop()
                res += drop * min(stack[-1], arr[i])
            stack.append(arr[i])
        while len(stack) > 2:
            res += stack.pop()*stack[-1]
        return res