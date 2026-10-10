class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0
        for i in set1:
            if i - 1 not in set1:
                count = 0
                j = i
                while j in set1:
                    count += 1
                    j += 1
                longest = max(longest, count)
        return longest