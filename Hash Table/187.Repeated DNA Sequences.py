# Solution 1: Sliding Window + Hash Table
# The idea is straight forward:
# 1. Move a sliding window of length L along the string of length N.
# 2. Check if the sequence in the sliding window is in the hashset of
# already seen sequences.
# If yes, we find one repeated sequence. Update the output.
# If not, save the sequence in the sliding window in the hashset.

# Time Complexity: O((N-L)L), where N is the length of s and L is the
# determined length of substrings.
# Space Complexity: O((N-L)L)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, output = set(), set()
        for start in range(n-L+1):
            tmp = s[start:start+L]
            if tmp in seen:
                output.add(tmp)
            seen.add(tmp)
        return output