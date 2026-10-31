class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        
        def backtrack(i, total):
            if total == target:
                res.append(current.copy())
                return

            if i == len(nums) or total > target:
                return

            current.append(nums[i])
            backtrack(i, total + nums[i])
            current.pop()
            backtrack(i + 1, total)
        backtrack(0, 0)
        return res
        