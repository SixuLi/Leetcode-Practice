# Solution 1: Hash Table and Heap
# First, we use a hash table to count the frequency of each number.
# And scan the whole hash table and use minHeap to maintain
# the top k frequent elements.

# Time Complexity: O(N + Nlogk)
# Space Complexity: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict = dict()
        for num in nums:
            if num in Dict:
                Dict[num] += 1
            else:
                Dict[num] = 1
        hp = []
        for num in Dict.keys():
            heapq.heappush(hp, (Dict[num], num))
            if len(hp) > k:
                heapq.heappop(hp)
        return [heapq.heappop(hp)[1] for i in range(k)]