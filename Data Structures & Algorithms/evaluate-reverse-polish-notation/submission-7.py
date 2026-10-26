class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '*', '-', '/']
        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    result = a + b
                if i == '-':
                    result = a - b
                if i == '*':
                    result = a * b
                if i == '/':
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[-1]
        