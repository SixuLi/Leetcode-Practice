# Solution 1: Hash Table
# Use hash table to collect all the alphabets in the given word and the postion of them.
# Find the first one the only appear once.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        Dict = dict()
        for index, alphabet in enumerate(s):
            if alphabet in Dict:
                Dict[alphabet].append(index)
            else:
                Dict[alphabet] = [index]
        first_unique = float('inf')
        for indexes in Dict.values():
            if len(indexes) == 1:
                first_unique = min(first_unique, indexes[0])
        return first_unique if first_unique != float('inf') else -1

# Solution 2: Improved Version

# Time Complexity: O(N)
# Space Complexity: O(1)

import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for index, ch in enumerate(s):
            if count[ch] == 1:
                return index
        return -1