class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right: #untill only one condition is remained
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # we need to check which half will have the smallest element
                left = mid + 1
            else:
                right = mid
        return nums[left]
        