class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = float('inf')
        for i in prices:
            min_value = min(min_value, i)
            max_profit = max(max_profit, i - min_value)
        return max_profit
        