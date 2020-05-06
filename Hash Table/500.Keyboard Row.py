# Solution 1:
# Use three sets to collect the alphabets on each line respectively.
# Scan all the words and determine whether current word is the subset of each line.

# Time Complexity: O(NL)
# Space Complexity: O(NL)

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = set('qwertyuiop')
        line2 = set('asdfghjkl')
        line3 = set('zxcvbnm')

        if not words:
            return []
        res = []
        for word in words:
            cur = set(word.lower())
            if cur <= line1 or cur <= line2 or cur <= line3:
                res.append(word)
        return res