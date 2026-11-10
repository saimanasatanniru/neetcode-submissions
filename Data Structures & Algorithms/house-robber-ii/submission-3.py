class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        case1 = self.rob_linear(nums[:-1])
        case2 = self.rob_linear(nums[1:])
        return max(case1, case2)

    def rob_linear(self, rob):
        prev2 = 0
        prev1 = 0
        for money in rob:
            current = max(money + prev2, prev1)
            prev2 = prev1
            prev1 = current
        return prev1
        