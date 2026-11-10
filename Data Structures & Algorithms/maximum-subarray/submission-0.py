class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], nums[i] + currSum)
            maxSum = max(maxSum, currSum)
        return maxSum
        