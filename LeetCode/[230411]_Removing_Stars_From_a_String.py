class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isalpha():
                stack.append(c)
            elif c == '*':
                stack.pop()
        return ''.join(stack)