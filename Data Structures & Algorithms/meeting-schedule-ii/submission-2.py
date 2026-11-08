"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort meetings by starting time
        intervals.sort(key=lambda x: x.start)

        # Min heap stores the ending times of occupied rooms
        min_heap = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # If the earliest meeting has finished,
            # reuse that meeting room
            if min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)

            # Add the current meeting's ending time
            heapq.heappush(min_heap, end)

        # Number of rooms required
        return len(min_heap)