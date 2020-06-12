# Solution 1: Insert Positions

# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Dict = Counter(tasks)
        max_freq = max(Dict.values())

        count = 0
        for task in Dict.keys():
            if Dict[task] == max_freq:
                count += 1

        partCount = max_freq - 1
        emptySlots = partCount * (n - (count - 1))
        availableTasks = len(tasks) - max_freq * count
        idles = max(0, emptySlots - availableTasks)

        return len(tasks) + idles