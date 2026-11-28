class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for temp in range(len(temperatures)):
            while stack and temperatures[temp] > temperatures[stack[-1]]:
                res[stack[-1]] = temp - stack[-1]
                stack.pop()
            stack.append(temp)
        return res
        