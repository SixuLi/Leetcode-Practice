# Solution 1: Hash Table

# Time Complexity: O(J.length + S.length)
# Space Complexity: O(S.length)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone = dict()
        for s in S:
            if s in stone:
                stone[s] += 1
            else:
                stone[s] = 1
        res = 0
        for j in J:
            if j in stone:
                res += stone[j]
        return res