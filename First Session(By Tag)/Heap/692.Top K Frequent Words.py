# Solution 1: Max Heap

# Time Complexity: O(nlogk)
# Space Complexity: O(n)

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return heapq.nsmallest(k, c, key = lambda word: (-c[word], word))