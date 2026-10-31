class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current, open, close):
            if open == n and close == n:
                res.append(current)

            if open < n:
                backtrack(current + '(', open + 1, close)
            if close < open:
                backtrack(current + ')', open, close + 1)
        backtrack("", 0, 0)
        return res
        