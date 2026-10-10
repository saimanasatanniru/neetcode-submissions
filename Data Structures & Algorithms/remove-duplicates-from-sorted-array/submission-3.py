class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                nums.pop(j)
        return len(nums)

        