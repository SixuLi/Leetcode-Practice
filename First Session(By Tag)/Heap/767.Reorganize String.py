# Solution 1: Max Heap and Hash Table
# Algorithm:
# 1. Say most frequently occurring character (say c) has frequency max_freq.
# Then arrange c leaving a space between consecutive c's. The remaining characters
# should be more than the number of space for a valid arrangement. This means
# That max_freq + (max_freq-1) <= len(S). We can test this quickly using Counter
# class from collections module.
# 2. Now we create an array called res to store the result. We add (-freq, char)
# tuples to a heap (build a max heap). We then pick the most frequent element and
# if that element is not the last element in the res, we add it to res. If it is
# the last element of the result, then we pick the second most frequent element
# and add it back to the heap if the frequency is not -1.

# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter
from heapq import *
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        max_freq = c.most_common(1)[0][1]
        if 2*max_freq - 1 > len(S):
            return ""
        heap = []
        for ch, freq in c.items():
            heappush(heap, (-freq, ch))
        res = []
        while heap:
            freq, ch = heappop(heap)
            if not res or ch != res[-1]:
                res.append(ch)
                if freq != -1:
                    heappush(heap, (freq+1, ch))
            else:
                freq1, ch1 = heappop(heap)
                res.append(ch1)
                heappush(heap, (freq, ch))
                if freq1 != -1:
                    heappush(heap, (freq1+1, ch1))
        return ''.join(res)
