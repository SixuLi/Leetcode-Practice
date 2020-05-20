# Solution 1: Merge Intervals with Two Pointers

# Time Complexity: O(M+N)
# Space Complexity: O(M+N)

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        pA, pB = 0, 0
        res = []
        while pA < len(A) and pB < len(B):
            lo = max(A[pA][0], B[pB][0])
            hi = min(A[pA][1], B[pB][1])

            if lo <= hi:
                res.append([lo, hi])

            if A[pA][1] <= B[pB][1]:
                pA += 1
            else:
                pB += 1
        return res
