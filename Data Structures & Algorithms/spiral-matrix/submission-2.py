class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []

        while top <= bottom and left <= right:

            # Traverse top row: left to right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # Traverse right column: top to bottom
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # Traverse bottom row: right to left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # Traverse left column: bottom to top
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res