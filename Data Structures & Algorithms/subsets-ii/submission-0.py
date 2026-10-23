class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        def backtrack(i):
            res.append(current.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                current.append(nums[j])
                backtrack(j + 1)
                current.pop()
        backtrack(0)
        return res
        