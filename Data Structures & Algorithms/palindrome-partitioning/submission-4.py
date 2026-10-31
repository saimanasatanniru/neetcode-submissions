class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []
        def backtrack(start):
            if start == len(s):
                res.append(current.copy())
                return
            for end in range(start, len(s)):
                substring = s[start : end + 1]
                if substring == substring[::-1]:
                    current.append(substring)
                    backtrack(end + 1)
                    current.pop()
        backtrack(0)
        return res
        
        