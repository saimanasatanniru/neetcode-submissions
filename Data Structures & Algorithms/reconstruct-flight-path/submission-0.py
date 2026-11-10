class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)

        for airport in graph:
            graph[airport].sort(reverse = True)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            result.append(airport)

        dfs("JFK")
        return result[::-1]
        