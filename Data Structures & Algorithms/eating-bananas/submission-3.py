class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 # atleast 1 banana it has to eat
        right = max(piles) # max value of the piles of bananas so we need to get the avg speed 

        while left < right:
            mid = (left + right) // 2 #speed
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        return left