class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        used = [False] * len(nums)
        def backtrack():
            if len(current) == len(nums):
                res.append(current.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                current.append(nums[i])
                used[i] = True
                backtrack()
                current.pop()
                used[i] = False
        backtrack()
        return res
        