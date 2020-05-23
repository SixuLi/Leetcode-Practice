# Solution 1: Use List(TLE)

# Time Complexity: O(n + logn) for addNum() and O(1) for findMedian()

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        if not self.data:
            self.data.append(num)
        else:
            lo, hi = 0, len(self.data)-1
            while lo <= hi:
                mid = (lo + hi) // 2
                if self.data[mid] == num:
                    lo = mid
                    break
                elif self.data[mid] > num:
                    hi = mid - 1
                else:
                    lo = mid + 1
            self.data.append(num)
            for i in range(len(self.data)-1, lo, -1):
                self.data[i] = self.data[i-1]
            self.data[lo] = num

    def findMedian(self) -> float:
        if len(self.data) % 2 == 1:
            return self.data[len(self.data) // 2]
        else:
            i = len(self.data) // 2
            return (self.data[i] + self.data[i-1]) / 2

# Solution 2: Two Heaps
# If we maintain two heaps in the following way:
# A max-Heap to store the smaller half of the input numbers.
# A min-Heap to store the larger half of the input numbers.
# This gives access to median values in the input: they comprise the top of the heaps.

# Time Complexity: O(logn) for addNum() and O(1) for findMedian()
# Space Complexity: O(n)

from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            heappush(self.maxHeap, -heappushpop(self.minHeap, num))
        else:
            heappush(self.minHeap, -heappushpop(self.maxHeap, -num))

    def findMedian(self) -> float:
        return -self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) \
            else (-self.maxHeap[0] + self.minHeap[0]) / 2





















