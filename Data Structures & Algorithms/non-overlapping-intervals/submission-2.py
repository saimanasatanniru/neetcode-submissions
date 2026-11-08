class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Sort intervals by ending time
        intervals.sort(key=lambda x: x[1])

        # Initially, keep the first interval
        count = 0
        prev_end = intervals[0][1]

        # Process remaining intervals
        for i in range(1, len(intervals)):

            # If current interval starts after or at previous end,
            # there is no overlap. Keep it.
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]

            else:
                # Overlap: remove the current interval
                count += 1

                # Keep the interval that finishes earlier
                prev_end = min(prev_end, intervals[i][1])

        return count