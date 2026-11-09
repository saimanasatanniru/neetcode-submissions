class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x : x[0])
        sorted_queries = sorted((query, i) for i, query in enumerate(queries))
        min_heap = []
        result = [-1] * len(queries)
        i = 0
        for query, original_index in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                length = end - start + 1
                heapq.heappush(min_heap, (length, end))
                i += 1

            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            if min_heap:
                result[original_index] = min_heap[0][0]

        return result        