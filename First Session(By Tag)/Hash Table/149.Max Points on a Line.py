# Solution 1:

# Time Complexity: O(N^2)
# Space Complexity: O(N)

import numpy as np
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        m = 0
        for i in range(l):
            Dict = {float('inf'):1}
            same = 0
            for j in range(i+1, l):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                    continue
                if points[i][0] == points[j][0]:
                    slope = float('inf')
                else:
                    slope = np.float128((points[i][1] - points[j][1])) / np.float128((points[i][0] - points[j][0]))
                if slope in Dict:
                    Dict[slope] += 1
                else:
                    Dict[slope] = 2
            m = max(m, max(Dict.values()) + same)
        return m