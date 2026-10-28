class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(maxheap, (dist, x, y))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [[x, y] for dist, x, y in maxheap]
        