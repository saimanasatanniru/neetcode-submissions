class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1, n + 1)}
        for source, destination, weight in times:
            graph[source].append((destination, weight))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        min_heap = [(0, k)]
        while min_heap:
            current_distance, node = heapq.heappop(min_heap)
            if current_distance > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_distance = current_distance + weight
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))
        max_distance = max(dist[1:])
        if max_distance == float('inf'):
            return -1
        return max_distance
        