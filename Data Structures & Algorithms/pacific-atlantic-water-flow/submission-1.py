class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Why greater than or equal? Normal water flows downhill or across equal heights. We’re searching backward from the ocean, so we can move from a cell to a neighbor that is higher or equally high.
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)


        #for pacific
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        #for atlantic
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        result = []
        for cell in pacific:
            if cell in atlantic:
                result.append(list(cell))

        return result
        