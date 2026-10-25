class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in set1:
                count = 1
                j = nums[i] + 1
                while j in set1:
                    j += 1
                    count += 1
                longest = max(longest, count)
        return longest
        