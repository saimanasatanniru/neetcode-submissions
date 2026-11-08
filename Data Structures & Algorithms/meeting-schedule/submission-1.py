class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Sort meetings by starting time
        intervals.sort(key=lambda x: x.start)

        # Compare adjacent meetings
        for i in range(1, len(intervals)):

            # If current meeting starts before previous ends,
            # there is a scheduling conflict
            if intervals[i].start < intervals[i - 1].end:
                return False

        # No overlapping meetings found
        return True