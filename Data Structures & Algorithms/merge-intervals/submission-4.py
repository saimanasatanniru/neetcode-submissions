class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals by their starting points.
        # This ensures that we always process the interval
        # with the smallest start first.
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:

            # If result is empty OR the current interval
            # starts after the previous interval ends,
            # there is no overlap. So append it.
            if not result or interval[0] > result[-1][1]:
                result.append(interval)

            else:
                # Intervals overlap, so merge them.
                #
                # We only update index 1 (ending point).
                # Why?
                # Because intervals are sorted by starting point.
                # Therefore, the existing interval's start is
                # already smaller than or equal to the current
                # interval's start.
                #
                # The starting point doesn't need to change.
                # Only the ending point might need to extend.
                result[-1][1] = max(
                    result[-1][1],
                    interval[1]
                )

        return result