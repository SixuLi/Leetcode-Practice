# Solution 1: Min Heap

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Initialize the heap
        used_room = []

        # Give a new room to the first meeting
        heapq.heappush(used_room, intervals[0][1])
        for interval in intervals[1:]:
            # When at the beginning of current meeting, the earliest ending meeting has ended,
            # free the earliest meeting.
            if interval[0] >= used_room[0]:
                heapq.heappop(used_room)
            heapq.heappush(used_room, interval[1])
        return len(used_room)