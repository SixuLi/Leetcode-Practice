# Solution 1: Hash Map + Max Heap

# Time Complexity: O(n+klogk), where k is the number of characters.
# Space Complexity: O(n)

from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        Freq = Counter(s)
        heap = []
        for ch, freq in Freq.items():
            heapq.heappush(heap, (-freq, ch))
        while heap:
            freq, ch = heapq.heappop(heap)
            res += ch * -freq
        return res