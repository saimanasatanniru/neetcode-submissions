class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            tempMax = currMax
            currMax = max(nums[i], nums[i] * tempMax, nums[i] * currMin)
            currMin = min(nums[i], nums[i] * tempMax, nums[i] * currMin)
            result = max(result, currMax)
        return result        
        