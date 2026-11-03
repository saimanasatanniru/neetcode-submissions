class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        