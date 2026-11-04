class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges.
        if len(edges) != n - 1:
            return False

        # Build an adjacency list for the undirected graph.
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                # Ignore the edge back to the node we came from.
                if neighbor == parent:
                    continue

                # A visited neighbor other than the parent means a cycle.
                if neighbor in visited:
                    return False

                # Explore this neighbor; pass the current node as its parent.
                if not dfs(neighbor, node):
                    return False

            return True

        # Start from node 0; it has no parent.
        # Also ensure every node was reached (the graph is connected).
        return dfs(0, -1) and len(visited) == n