class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        current = []
        def backtrack(i, total):
            if total == target:
                res.append(current.copy())
                return

            if total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                current.append(candidates[j])
                backtrack(j + 1, total + candidates[j])
                current.pop()
        backtrack(0, 0)
        return res
        