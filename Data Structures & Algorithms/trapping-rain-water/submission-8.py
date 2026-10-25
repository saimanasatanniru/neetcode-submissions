class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        leftMax = 0
        rightMax = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax: #the current bar is greater then the left max we will not collect water here because we can guarantee the more water collection
                    leftMax = height[left]
                else:
                    water += (leftMax - height[left])
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    water += (rightMax - height[right])
                right -= 1
        return water
        