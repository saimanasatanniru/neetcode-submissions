class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    result =  a + b
                if token == '-':
                    result = a - b
                if token == '*':
                    result = a * b
                if token == '/':
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
        