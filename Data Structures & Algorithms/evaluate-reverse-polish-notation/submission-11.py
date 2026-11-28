class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []
        for c in tokens:
            if c in operands:
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    result = a + b
                elif c == '-':
                    result = a - b
                elif c == '*':
                    result = a * b
                elif c == '/':
                    result = int(a / b)
                stack.append(int(result))       
            else:
                stack.append(int(c))
        return stack[-1]

        