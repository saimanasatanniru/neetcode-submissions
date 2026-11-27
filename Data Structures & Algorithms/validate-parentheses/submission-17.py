class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {']' : '[', '}' : '{', ')' : '('}
        for token in s:
            if token in pairs:
                if not stack or pairs[token] != stack.pop():
                    return False
            else:
                stack.append(token)
        return len(stack) == 0
        