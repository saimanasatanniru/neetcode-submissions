class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] != word[index]:
                return False

            original_char = board[row][col]
            board[row][col] = '#'
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if backtrack(new_row, new_col, index + 1):
                    board[row][col] = original_char
                    return True
            board[row][col] = original_char
            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True

        return False
        