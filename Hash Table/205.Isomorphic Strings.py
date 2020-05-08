# Solution 1: Hash Map

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for idx, alphabet in enumerate(s):
            d1[alphabet] = d1.get(alphabet, []) + [idx]
        for idx, alphabet in enumerate(t):
            d2[alphabet] = d2.get(alphabet, []) + [idx]
        return sorted(d1.values()) == sorted(d2.values())

# Solution 2: Encode the string
# Use Hash Map to encode each string.

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def encode(s):
            d = {}
            encoded = []
            for ch in s:
                if ch not in d:
                    d[ch] = len(d)
                encoded.append(d[ch])
            return str(encoded)
        return encode(s) == encode(t)