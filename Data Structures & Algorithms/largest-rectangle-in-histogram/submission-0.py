class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i #current_index - previous_index - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            max_area = max(max_area, height * width)
        
        return max_area
        