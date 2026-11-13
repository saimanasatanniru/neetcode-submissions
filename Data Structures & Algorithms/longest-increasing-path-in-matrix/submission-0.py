class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            memo[(r, c)] = res
            return res
        answer = 0
        for r in range(m):
            for c in range(n):
                answer = max(answer, dfs(r, c))
        return answer