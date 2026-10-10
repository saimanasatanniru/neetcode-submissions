class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        set1 = set(nums)

        for i in nums:
            if i - 1 not in set1:
                j = i
                maxN = 1
                while j + 1 in set1:
                    maxN += 1
                    j += 1
                res = max(res, maxN)
        return res
    
        