# Solution 1: Two Pointers

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        # Find last position of each element in S.
        last = {c: i for i, c in enumerate(S)}
        start = end = 0
        res = []
        for i, c in enumerate(S):
            # Expand current partition.
            end = max(end, last[c])

            # Find a partition.
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res